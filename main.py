from src.data_loader import load_data
from src.monthly_aggregation import compute_monthly_ohlc
from src.indicators import add_technical_indicators
from src.writer import write_partitioned_outputs


def main():
    # Input CSV path or URL
    DATA_SOURCE = "https://raw.githubusercontent.com/sandeep-tt/tt-intern-dataset/main/historical_stock_prices.csv"

    # Output directory
    OUTPUT_DIR = "outputs"

    # Step 1: Load and prepare daily data
    df = load_data(DATA_SOURCE)

    # Step 2: Compute monthly OHLC aggregates
    monthly_df = compute_monthly_ohlc(df)

    # Step 3: Add technical indicators (SMA & EMA)
    final_df = add_technical_indicators(monthly_df)

    # Step 4: Write partitioned CSV outputs
    write_partitioned_outputs(final_df, OUTPUT_DIR)

    print("Processing completed successfully. Output files are available in the 'outputs/' directory.")


if __name__ == "__main__":
    main()

