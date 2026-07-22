from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.data_processing.csv_reader import read_csv
from app.data_processing.summary import dataset_summary

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed.",
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    df = read_csv(file_path)

    summary = dataset_summary(df)

    return {
        "message": "CSV uploaded successfully.",
        "filename": file.filename,
        "summary": summary,
    }