import pandas as pd

def load_parquet(path):
    df = pd.read_parquet(path)
    return df

def extract_price_panel(df, price_type):
    
    if price_type not in df.columns:
        raise ValueError(f"{price_type} not found in dataframe columns: {df.columns.tolist()}")

    panel = df.pivot(index="Date", columns="Ticker", values=price_type)
    panel = panel.sort_index()
    panel = panel.reindex(sorted(panel.columns), axis=1)
    return panel

def basic_clean(panel):
    panel = panel.ffill().bfill()
    panel = panel.dropna(axis=1, how="all")
    return panel

