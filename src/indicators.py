import pandas as pd


def add_technical_indicators(monthly_df: pd.DataFrame) -> pd.DataFrame:
    """
    Add SMA and EMA technical indicators based on monthly closing prices.

    Parameters
    ----------
    monthly_df : pd.DataFrame
        Monthly OHLC data per ticker.

    Returns
    -------
    pd.DataFrame
        DataFrame with SMA and EMA indicators added.
    """
    # Ensure correct ordering before rolling calculations
    monthly_df = monthly_df.sort_values(by=["ticker", "date"])

    # Simple Moving Averages
    monthly_df["SMA_10"] = (
        monthly_df
        .groupby("ticker")["close"]
        .rolling(window=10)
        .mean()
        .reset_index(level=0, drop=True)
    )

    monthly_df["SMA_20"] = (
        monthly_df
        .groupby("ticker")["close"]
        .rolling(window=20)
        .mean()
        .reset_index(level=0, drop=True)
    )

    # Exponential Moving Averages
    monthly_df["EMA_10"] = (
        monthly_df
        .groupby("ticker")["close"]
        .ewm(span=10, adjust=False)
        .mean()
        .reset_index(level=0, drop=True)
    )

    monthly_df["EMA_20"] = (
        monthly_df
        .groupby("ticker")["close"]
        .ewm(span=20, adjust=False)
        .mean()
        .reset_index(level=0, drop=True)
    )

    return monthly_df

