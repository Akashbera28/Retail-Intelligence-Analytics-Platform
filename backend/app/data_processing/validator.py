import pandas as pd


REQUIRED_COLUMNS = [
    "Order ID",
    "Order Date",
    "Sales",
    "Profit",
]


def validate_dataset(df: pd.DataFrame) -> dict:
    """
    Validate the uploaded retail dataset.
    """

    validation = {}

    # Required columns
    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    validation["required_columns_present"] = len(missing_columns) == 0
    validation["missing_required_columns"] = missing_columns

    # Missing values
    validation["missing_values"] = int(df.isnull().sum().sum())

    # Duplicate rows
    validation["duplicate_rows"] = int(df.duplicated().sum())

    # Negative sales
    if "Sales" in df.columns:
        validation["negative_sales"] = int((df["Sales"] < 0).sum())
    else:
        validation["negative_sales"] = 0

    # Negative profit
    if "Profit" in df.columns:
        validation["negative_profit"] = int((df["Profit"] < 0).sum())
    else:
        validation["negative_profit"] = 0

    return validation