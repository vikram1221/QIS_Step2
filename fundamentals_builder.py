import yfinance as yf
import pandas as pd
import os 
import time

base_dir = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2"
sp500_path = os.path.join(base_dir, "SP500.csv")
output_path = os.path.join(base_dir, "fundamentals.csv")

def clean_ticker(ticker):
    return ticker.replace(".", "-")

def download_fundamentals(ticker):

    try:
        t = yf.Ticker(ticker)
        info = t.info
    
        return {
            "Symbol"    : ticker,
            "PE"        : info.get("trailingPE", None),
            "ForwardPE" : info.get("forwardPE", None),
            "PB"        : info.get("priceToBook", None),
            "EV_EBITDA" : info.get("enterpriseToEbitda", None), 
            "MarketCap" : info.get("marketCap", None)
        }
    except Exception as e:
        print(f"Error for {ticker}: {e}")
        return None
    
def main():
    df = pd.read_csv(sp500_path)
    tickers = df["Symbol"].dropna().unique().tolist()
    tickers = [clean_ticker(t) for t in tickers]

    all_data = []

    print(f"Downloading fundamentals for {len(tickers)} tickers...")

    for t in tickers:
        print(f"--> {t}")
        data = download_fundamentals(t)
        if data:
            all_data.append(data)
        time.sleep(0.2)
    
    fundamentals_df = pd.DataFrame(all_data)
    fundamentals_df.to_csv(output_path, index=False)

    print("\nSaved fundamentals to: ", output_path)
    print(fundamentals_df.head())

if __name__ == "__main__":
    main()