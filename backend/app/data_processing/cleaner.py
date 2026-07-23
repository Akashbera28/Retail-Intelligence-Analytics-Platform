from pathlib import Path

import pandas as pd

from app.data_processing.csv_reader import read_csv


def clean_sales_data(input_path: str, output_path: str) -> dict:
    """
    Load, validate and clean a retail sales CSV file.
    """

    input_file = Path(input_path)
    output_file = Path(output_path)

    if not input_file.exists():
        raise FileNotFoundError(
            f"CSV file not found: {input_path}"
        )

    # Read CSV using the project's CSV reader
    df = read_csv(input_file)

    original_rows = len(df)
    original_columns = len(df.columns)

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Remove completely empty rows and columns
    df.dropna(how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)

    # Remove duplicate rows
    duplicate_rows = int(df.duplicated().sum())
    df.drop_duplicates(inplace=True)

    # Convert date columns
    date_columns = [
        "Order Date",
        "Ship Date",
    ]

    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce",
                dayfirst=True,
            )

    # Convert numeric columns
    numeric_columns = [
        "Sales",
        "Profit",
        "Discount",
        "Order Quantity",
        "Unit Price",
        "Shipping Cost",
        "Product Base Margin",
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce",
            )

    # Remove rows missing essential values
    essential_columns = [
        column
        for column in ["Sales", "Profit"]
        if column in df.columns
    ]

    if essential_columns:
        df.dropna(
            subset=essential_columns,
            inplace=True,
        )

    # Fill missing categorical values
    categorical_columns = df.select_dtypes(
        include=["object", "string"]
    ).columns

    for column in categorical_columns:
        df[column] = (
            df[column]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
        )

    # Fill remaining numeric NaN values
    numeric_columns = df.select_dtypes(
        include=["number"]
    ).columns

    for column in numeric_columns:
        df[column] = df[column].fillna(0)

    # Save cleaned dataset
    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        output_file,
        index=False,
        date_format="%Y-%m-%d",
        encoding="utf-8",
    )

    return {
        "message": "Dataset cleaned successfully.",
        "original_rows": original_rows,
        "cleaned_rows": len(df),
        "removed_rows": original_rows - len(df),
        "original_columns": original_columns,
        "final_columns": len(df.columns),
        "duplicate_rows_removed": duplicate_rows,
        "missing_values_remaining": int(
            df.isnull().sum().sum()
        ),
        "output_file": str(output_file),
    }