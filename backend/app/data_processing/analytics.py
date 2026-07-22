import pandas as pd


def calculate_kpis(df: pd.DataFrame) -> dict:
    """
    Calculate business KPIs and dashboard analytics.
    """

    analytics = {}

    # ==========================
    # KPI Section
    # ==========================

    analytics["total_sales"] = round(
        float(df["Sales"].fillna(0).sum()), 2
    ) if "Sales" in df.columns else 0.0

    analytics["total_profit"] = round(
        float(df["Profit"].fillna(0).sum()), 2
    ) if "Profit" in df.columns else 0.0

    analytics["total_orders"] = (
        int(df["Order ID"].nunique())
        if "Order ID" in df.columns
        else len(df)
    )

    if "Order Quantity" in df.columns:
        analytics["total_quantity"] = int(
            df["Order Quantity"].fillna(0).sum()
        )
    elif "Quantity" in df.columns:
        analytics["total_quantity"] = int(
            df["Quantity"].fillna(0).sum()
        )
    else:
        analytics["total_quantity"] = 0

    analytics["average_order_value"] = round(
        analytics["total_sales"] /
        analytics["total_orders"],
        2
    ) if analytics["total_orders"] else 0.0

    # ==========================
    # Sales by Region
    # ==========================

    if "Region" in df.columns:
        analytics["sales_by_region"] = (
            df.groupby("Region")["Sales"]
            .sum()
            .round(2)
            .to_dict()
        )
    else:
        analytics["sales_by_region"] = {}

    # ==========================
    # Sales by Category
    # ==========================

    category_col = None

    if "Category" in df.columns:
        category_col = "Category"

    elif "Product Category" in df.columns:
        category_col = "Product Category"

    if category_col:
        analytics["sales_by_category"] = (
            df.groupby(category_col)["Sales"]
            .sum()
            .round(2)
            .to_dict()
        )
    else:
        analytics["sales_by_category"] = {}

    # ==========================
    # Top 10 Products
    # ==========================

    product_col = None

    if "Product Name" in df.columns:
        product_col = "Product Name"

    if product_col:
        analytics["top_products"] = (
            df.groupby(product_col)["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .round(2)
            .to_dict()
        )
    else:
        analytics["top_products"] = {}

    return analytics