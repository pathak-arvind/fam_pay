import pandas as pd


def load_data(csv_path: str) -> pd.DataFrame:
    """
    Load stock price data from a CSV file or URL,
    parse dates, and sort by ticker and date.

    Parameters
    ----------
    csv_path : str
        Path or URL to the input CSV file.

    Returns
    -------
    pd.DataFrame
        Cleaned and sorted DataFrame.
    """
    df = pd.read_csv(csv_path)

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Sort by ticker and date to ensure correct time ordering
    df = df.sort_values(by=["ticker", "date"])

    return df

