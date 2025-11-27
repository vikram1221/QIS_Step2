import pandas as pd
import glob
import os
from csv_downloader import load_tickers
from downloader import download_prices

def combine_raw_prices(folder, save_path):
    all_files = glob.glob(os.path.join(folder, "*.csv"))
    dfs = []

    for file in all_files:
        ticker = os.path.basename(file).replace(".csv", "")
        df = pd.read_csv(file)

        # FIX: drop corrupt first row
        df = df.iloc[1:].reset_index(drop=True)

        df["Ticker"] = ticker
        dfs.append(df)

    combined = pd.concat(dfs, ignore_index=True)
    combined.to_parquet(save_path, index=False)
    print("Saved:", save_path)
    return combined


def main():
    #Defining path
    path = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2\SP500.csv"

    #Loading tickers 
    tickers = load_tickers(path)
    print(f"Loaded {len(tickers)} tickers")

    #Dowloading price data
    download_prices(
        tickers, 
        start="2020-01-01",
        folder=r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2\raw_prices"
    )

    folder = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2\raw_prices"
    save_path = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2\all_prices.parquet"

    df = combine_raw_prices(folder, save_path)
    print(df.head())

if __name__=="__main__":
    main()

# path = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2\all_prices.parquet"
# df = pd.read_parquet(path)
# print(df.shape)
# print(df.head())