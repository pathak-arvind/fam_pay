# Data Engineering Internship Assignment – FamPay

## Overview

This project implements a modular Python (Pandas) pipeline to transform daily stock price data into monthly summaries and compute technical indicators. The objective is to provide a macro-level view of stock performance over a two-year period, following clean data engineering practices.

## Dataset

- Source: https://github.com/sandeep-tt/tt-intern-dataset  
- Input contains daily stock prices for 10 tickers:  
  AAPL, AMD, AMZN, AVGO, CSCO, MSFT, NFLX, PEP, TMUS, TSLA  
- Time span: 2 years (daily frequency)

## Processing Pipeline

The solution is implemented in a modular manner and consists of the following stages:

1. Data Loading & Preparation  
   - Load CSV data from source  
   - Convert the `date` column to datetime format  
   - Sort data by `ticker` and `date`

2. Monthly Aggregation  
   Daily stock prices are resampled to monthly frequency per ticker using:
   - Open: First trading day of the month  
   - Close: Last trading day of the month  
   - High: Maximum price within the month  
   - Low: Minimum price within the month  
   - Volume: Monthly sum  

3. Technical Indicators  
   The following indicators are computed using monthly closing prices:
   - Simple Moving Average (SMA 10, SMA 20)  
   - Exponential Moving Average (EMA 10, EMA 20)  
   All calculations use vectorized Pandas operations without any third-party technical analysis libraries.

4. Output Generation  
   - One CSV file is generated per ticker  
   - Each output file contains exactly 24 rows (one per month)  
   - File naming convention: `result_{TICKER}.csv`

## Project Structure

fam_pay/
- src/
  - data_loader.py
  - monthly_aggregation.py
  - indicators.py
  - writer.py
- outputs/
  - result_AAPL.csv
  - result_AMD.csv
  - ...
  - result_TSLA.csv
- main.py
- requirements.txt
- .gitignore
- LICENSE
- README.md

## How to Run

Run the following command from the project root:

python main.py

This executes the full pipeline and generates all output CSV files in the `outputs/` directory.

## Assumptions

- Monthly Open and Close prices are taken as the first and last trading days of the month respectively.  
- High and Low represent the monthly maximum and minimum prices.  
- Volume is aggregated as a monthly sum.  
- Technical indicators are calculated strictly on monthly closing prices.  
- Initial SMA values are NaN due to insufficient historical data.  
- The `adjclose` column is not used, as the assignment specifies calculations based on closing prices.

## Tools & Libraries

- Python  
- Pandas  

## Notes

The outputs were generated using this pipeline in a Google Colab environment and committed to the repository for verification.
