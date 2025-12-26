import os
import pandas as pd


def write_partitioned_outputs(df: pd.DataFrame, output_dir: str) -> None:
    """
    Write one CSV file per ticker symbol.

    Parameters
    ----------
    df : pd.DataFrame
        Final monthly data with technical indicators.
    output_dir : str
        Directory where output CSV files will be written.
    """
    os.makedirs(output_dir, exist_ok=True)

    for ticker in df["ticker"].unique():
        ticker_df = df[df["ticker"] == ticker].copy()

        # Drop ticker column for cleaner output
        ticker_df = ticker_df.drop(columns=["ticker"])

        file_path = os.path.join(output_dir, f"result_{ticker}.csv")
        ticker_df.to_csv(file_path, index=False)

