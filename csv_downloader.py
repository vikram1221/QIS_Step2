import pandas as pd

def load_tickers(path):
    df = pd.read_csv(path)
    tickers = df["Symbol"].dropna().unique().tolist()
    tickers = [ticker.replace(".", "-") for ticker in tickers]
    return tickers


our_path = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2\SP500.csv"
print(load_tickers(our_path))