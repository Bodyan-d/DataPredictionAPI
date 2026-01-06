import pandas as pd

class AnalyticsService:
    def __init__(self, data: list[dict]):
        self.df = pd.DataFrame(data)

    def summary(self) -> dict:
        if self.df.empty:
            return {
                "total_quantity": 0,
                "average_quantity": 0,
                "total_revenue": 0
            }

        return {
            "total_quantity": int(self.df["quantity"].sum()),
            "average_quantity": float(self.df["quantity"].mean()),
            "total_revenue": float(
                (self.df["quantity"] * self.df["price"]).sum()
            )
        }

    def daily_stats(self) -> list[dict]:
        if self.df.empty:
            return []

        grouped = (
            self.df
            .groupby("date")
            .agg(
                total_quantity=("quantity", "sum"),
                avg_price=("price", "mean")
            )
            .reset_index()
        )

        return grouped.to_dict(orient="records")
