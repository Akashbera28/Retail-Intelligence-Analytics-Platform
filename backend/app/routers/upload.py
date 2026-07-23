from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.data_processing.csv_reader import read_csv
from app.data_processing.summary import dataset_summary
from app.data_processing.validator import validate_dataset
from app.data_processing.analytics import calculate_kpis

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[3]

# Save uploaded CSVs here
UPLOAD_DIR = BASE_DIR / "data" / "raw"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/csv")
async def upload_csv(file: UploadFile = File(...)):
    """
    Upload a CSV file, validate it, and return summary + KPIs.
    """

    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed."
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        df = read_csv(file_path)

        summary = dataset_summary(df)
        validation = validate_dataset(df)
        analytics = calculate_kpis(df)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error processing CSV: {str(e)}"
        )

    return {
        "message": "CSV uploaded successfully.",
        "saved_path": str(file_path),
        "filename": file.filename,
        "summary": summary,
        "validation": validation,
        "analytics": analytics
    }