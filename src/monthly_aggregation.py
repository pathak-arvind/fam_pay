import pandas as pd


def compute_monthly_ohlc(df: pd.DataFrame) -> pd.DataFrame:
    """
    Resample daily stock data to monthly frequency and compute OHLC values.

    Parameters
    ----------
    df : pd.DataFrame
        Daily stock price data with columns including
        ['date', 'ticker', 'open', 'high', 'low', 'close', 'volume'].

    Returns
    -------
    pd.DataFrame
        Monthly aggregated OHLC data per ticker.
    """
    # Ensure date is the index for resampling
    df = df.set_index("date")

    monthly_df = (
        df
        .groupby("ticker")
        .resample("M")
        .agg({
            "open": "first",
            "high": "max",
            "low": "min",
            "close": "last",
            "volume": "sum"
        })
        .reset_index()
    )

    return monthly_df

