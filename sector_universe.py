import pandas as pd

class SectorUniverse:
    def __init__(self, sp500_path):
        df = pd.read_csv(sp500_path)

        # Use the columns your file actually has
        df = df[["Symbol", "Sector"]].dropna()

        # Replace dots with hyphens (BRK.B → BRK-B)
        df["Symbol"] = df["Symbol"].str.replace(".", "-", regex=False)

        self.df = df
        self.ticker_to_sector = dict(zip(df["Symbol"], df["Sector"]))

    def get_sector_tickers(self, sector_name):
        mask = self.df["Sector"] == sector_name
        return self.df.loc[mask, "Symbol"].tolist()

    def sector_of(self, ticker):
        return self.ticker_to_sector.get(ticker)


# if __name__ == "__main__":
#     import os
    
#     base_dir = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2"
#     sp500_path = os.path.join(base_dir, "SP500.csv")
#     panels_dir = os.path.join(base_dir, "panels")
#     ret_path = os.path.join(panels_dir, "returns_panel.parquet")

#     universe = SectorUniverse(sp500_path)
#     rets = pd.read_parquet(ret_path)

#     sector_name = "Financials"
#     sector_tickers = universe.get_sector(sector_name)
#     sector_tickers = [ticker for ticker in sector_tickers if ticker in rets.columns]
    
#     sector_rets = rets[sector_tickers]

#     print(f"Sector: {sector_name}")
#     print("Tickers in sector (in panel): ", len(sector_tickers))
#     print("Sector returns shape: ", sector_rets.shape)
#     print(sector_rets.head())