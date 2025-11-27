import yfinance as yf
import pandas as pd
import os

def download_prices(tickers, start="2020-01-01", end=None, folder=r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2\raw_prices"):

    os.makedirs(folder, exist_ok=True)
    all_data = []

    for ticker in tickers:
        print(f"Downloading data for {ticker}...")
        try:
            df = yf.download(ticker, start=start, end=end, progress=False)
            
            if df.empty:
                print(f"No data found for {ticker}, skip")
                continue
        
            df.reset_index(inplace=True)
            df["ticker"] = ticker

            df.to_csv(f"{folder}/{ticker}.csv", index=False)
            all_data.append(df)
        
        except Exception as e:
            print(f"Error downloading {ticker}: {e}")

    if not all_data:
        raise ValueError("No data downloaded. Check internet or ticker symbols")
        
    combined = pd.concat(all_data, ignore_index=True)
    return combined