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

# Upload directory
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/csv")
async def upload_csv(file: UploadFile = File(...)):
    """
    Upload a CSV file, analyze it, and return
    dataset summary, validation report, and KPIs.
    """

    # Validate file extension
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed."
        )

    # Save uploaded file
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Read CSV
        df = read_csv(file_path)

        # Dataset summary
        summary = dataset_summary(df)

        # Dataset validation
        validation = validate_dataset(df)

        # Business KPIs
        analytics = calculate_kpis(df)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error processing CSV: {str(e)}"
        )

    return {
        "message": "CSV uploaded successfully.",
        "filename": file.filename,
        "summary": summary,
        "validation": validation,
        "analytics": analytics
    }