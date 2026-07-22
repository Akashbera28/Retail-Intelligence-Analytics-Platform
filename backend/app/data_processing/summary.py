import pandas as pd


def dataset_summary(df: pd.DataFrame) -> dict:
    """
    Generate a summary of the uploaded dataset.
    """

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "data_types": {
            col: str(dtype)
            for col, dtype in df.dtypes.items()
        },
    }