from pathlib import Path

import pandas as pd


class SalesAnalyticsService:
    def __init__(self, csv_path: str):
        self.csv_path = Path(csv_path)

        if not self.csv_path.exists():
            raise FileNotFoundError(
                f"Processed dataset not found: {csv_path}"
            )

        self.df = pd.read_csv(self.csv_path)

        self.df.columns = self.df.columns.str.strip()

        if "Order Date" in self.df.columns:
            self.df["Order Date"] = pd.to_datetime(
                self.df["Order Date"],
                errors="coerce"
            )

        numeric_columns = [
            "Sales",
            "Profit",
            "Discount",
            "Order Quantity",
            "Unit Price",
            "Shipping Cost"
        ]

        for column in numeric_columns:
            if column in self.df.columns:
                self.df[column] = pd.to_numeric(
                    self.df[column],
                    errors="coerce"
                ).fillna(0)

    def get_kpis(self) -> dict:
        total_sales = (
            float(self.df["Sales"].sum())
            if "Sales" in self.df.columns
            else 0
        )

        total_profit = (
            float(self.df["Profit"].sum())
            if "Profit" in self.df.columns
            else 0
        )

        total_quantity = (
            int(self.df["Order Quantity"].sum())
            if "Order Quantity" in self.df.columns
            else 0
        )

        total_orders = (
            int(self.df["Order ID"].nunique())
            if "Order ID" in self.df.columns
            else len(self.df)
        )

        average_order_value = (
            total_sales / total_orders
            if total_orders > 0
            else 0
        )

        profit_margin = (
            total_profit / total_sales * 100
            if total_sales > 0
            else 0
        )

        return {
            "total_sales": round(total_sales, 2),
            "total_profit": round(total_profit, 2),
            "total_orders": total_orders,
            "total_quantity": total_quantity,
            "average_order_value": round(
                average_order_value,
                2
            ),
            "profit_margin_percentage": round(
                profit_margin,
                2
            )
        }

    def group_sales(self, column: str) -> list[dict]:
        if column not in self.df.columns:
            raise ValueError(
                f"Column '{column}' not found in dataset."
            )

        aggregation = {}

        if "Sales" in self.df.columns:
            aggregation["Sales"] = "sum"

        if "Profit" in self.df.columns:
            aggregation["Profit"] = "sum"

        if not aggregation:
            return []

        result = (
            self.df.groupby(column, dropna=False)
            .agg(aggregation)
            .reset_index()
        )

        sort_column = (
            "Sales"
            if "Sales" in result.columns
            else "Profit"
        )

        result = result.sort_values(
            by=sort_column,
            ascending=False
        )

        numeric_result_columns = [
            column_name
            for column_name in ["Sales", "Profit"]
            if column_name in result.columns
        ]

        for numeric_column in numeric_result_columns:
            result[numeric_column] = result[
                numeric_column
            ].round(2)

        return result.to_dict(orient="records")

    def get_monthly_sales(self) -> list[dict]:
        if "Order Date" not in self.df.columns:
            raise ValueError(
                "Order Date column not found in dataset."
            )

        dated_df = self.df.dropna(
            subset=["Order Date"]
        ).copy()

        dated_df["Month"] = dated_df[
            "Order Date"
        ].dt.to_period("M").astype(str)

        aggregation = {}

        if "Sales" in dated_df.columns:
            aggregation["Sales"] = "sum"

        if "Profit" in dated_df.columns:
            aggregation["Profit"] = "sum"

        if not aggregation:
            return []

        monthly_data = (
            dated_df.groupby("Month")
            .agg(aggregation)
            .reset_index()
            .sort_values("Month")
        )

        for column in ["Sales", "Profit"]:
            if column in monthly_data.columns:
                monthly_data[column] = monthly_data[
                    column
                ].round(2)

        return monthly_data.to_dict(orient="records")

    def get_top_products(self, limit: int = 10) -> list[dict]:
        product_column = None

        possible_product_columns = [
            "Product Name",
            "Product Sub-Category",
            "Product Category"
        ]

        for column in possible_product_columns:
            if column in self.df.columns:
                product_column = column
                break

        if product_column is None:
            raise ValueError(
                "No product-related column found."
            )

        aggregation = {}

        if "Sales" in self.df.columns:
            aggregation["Sales"] = "sum"

        if "Profit" in self.df.columns:
            aggregation["Profit"] = "sum"

        if not aggregation:
            return []

        result = (
            self.df.groupby(product_column)
            .agg(aggregation)
            .reset_index()
        )

        sort_column = (
            "Sales"
            if "Sales" in result.columns
            else "Profit"
        )

        result = result.sort_values(
            sort_column,
            ascending=False
        ).head(limit)

        for column in ["Sales", "Profit"]:
            if column in result.columns:
                result[column] = result[column].round(2)

        return result.to_dict(orient="records")