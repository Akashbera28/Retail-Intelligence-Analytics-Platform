from pathlib import Path

from fastapi import APIRouter, HTTPException, Query

from app.data_processing.cleaner import clean_sales_data
from app.services.analytics_service import SalesAnalyticsService


router = APIRouter(
    prefix="/analytics",
    tags=["Sales Analytics"]
)

BASE_DIR = Path(__file__).resolve().parents[3]

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"


def get_raw_file(filename: str) -> Path:
    safe_filename = Path(filename).name
    return RAW_DATA_DIR / safe_filename


def get_processed_file(filename: str) -> Path:
    safe_filename = Path(filename).name
    return PROCESSED_DATA_DIR / safe_filename


@router.post("/clean/{filename}")
def clean_dataset(filename: str):
    try:
        input_path = get_raw_file(filename)

        output_filename = f"cleaned_{Path(filename).name}"
        output_path = get_processed_file(output_filename)

        return clean_sales_data(
            input_path=str(input_path),
            output_path=str(output_path)
        )

    except FileNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        ) from error

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Data cleaning failed: {str(error)}"
        ) from error


@router.get("/kpis/{filename}")
def get_kpis(filename: str):
    try:
        file_path = get_processed_file(filename)
        service = SalesAnalyticsService(str(file_path))

        return {
            "message": "KPIs generated successfully.",
            "kpis": service.get_kpis()
        }

    except FileNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        ) from error

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        ) from error


@router.get("/category/{filename}")
def category_analysis(filename: str):
    try:
        service = SalesAnalyticsService(
            str(get_processed_file(filename))
        )

        return {
            "group_by": "Product Category",
            "data": service.group_sales(
                "Product Category"
            )
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        ) from error


@router.get("/region/{filename}")
def region_analysis(filename: str):
    try:
        service = SalesAnalyticsService(
            str(get_processed_file(filename))
        )

        return {
            "group_by": "Region",
            "data": service.group_sales("Region")
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        ) from error


@router.get("/segment/{filename}")
def segment_analysis(filename: str):
    try:
        service = SalesAnalyticsService(
            str(get_processed_file(filename))
        )

        return {
            "group_by": "Customer Segment",
            "data": service.group_sales(
                "Customer Segment"
            )
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        ) from error


@router.get("/monthly/{filename}")
def monthly_analysis(filename: str):
    try:
        service = SalesAnalyticsService(
            str(get_processed_file(filename))
        )

        return {
            "message": "Monthly analytics generated.",
            "data": service.get_monthly_sales()
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        ) from error


@router.get("/top-products/{filename}")
def top_products(
    filename: str,
    limit: int = Query(default=10, ge=1, le=100)
):
    try:
        service = SalesAnalyticsService(
            str(get_processed_file(filename))
        )

        return {
            "limit": limit,
            "data": service.get_top_products(limit)
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        ) from error