import pandas as pd

class PredictionService:
    def __init__(self, data: list[dict]):
        self.df = pd.DataFrame(data)

    def moving_average(self, window: int = 7) -> float:
        if self.df.empty:
            return 0.0
 
        if len(self.df) < window:
            return float(self.df["quantity"].mean())

        return float(
            self.df["quantity"]
            .rolling(window)
            .mean()
            .iloc[-1]
        )
