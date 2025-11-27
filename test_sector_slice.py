import os
import pandas as pd
from sector_universe import SectorUniverse   

base_dir = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2"
sp500_path = os.path.join(base_dir, "sp500.csv")
panels_dir = os.path.join(base_dir, "panels")
ret_path = os.path.join(panels_dir, "returns_panel.parquet")

def main():
    universe = SectorUniverse(sp500_path)
    rets = pd.read_parquet(ret_path)

    sector_name = "Financials"
    sector_tickers = universe.get_sector_tickers(sector_name)

    sector_tickers = [ticker for ticker in sector_tickers if ticker in rets.columns]

    sector_rets = rets[sector_tickers]

    print(f"Sector: {sector_name}")
    print("Tickers in sector (in panel): ", len(sector_tickers))
    print("Sector returns shape: ", sector_rets.shape)
    print(sector_rets.head())

if __name__ == "__main__":
    main()
