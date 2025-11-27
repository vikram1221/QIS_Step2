import os
import pandas as pd
from sector_universe import SectorUniverse

#Paths for files and folders

base_dir = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2"
sp500_path = os.path.join(base_dir, "SP500.csv")
fund_path = os.path.join(base_dir, "fundamentals.csv")
panels_dir = os.path.join(base_dir, "panels")
returns_path = os.path.join(panels_dir, "returns_panel.parquet")


#Loading fundamentals

def load_fundamentals(path=fund_path):
  
    df = pd.read_csv(path)
    df = df[["Symbol", "PE"]].dropna()
    df["Symbol"] = df["Symbol"].str.replace(".", "-", regex=False)
    df["PE"] = pd.to_numeric(df["PE"], errors="coerce")
    df = df.dropna(subset=["PE"])

    return df

def build_value_signal(sector_name="Financials"):
    universe = SectorUniverse(sp500_path)
    fund = load_fundamentals()
    sector_tickers = universe.get_sector_tickers(sector_name)
    sector_fund = fund[fund["Symbol"].isin(sector_tickers)].copy()

    sector_fund["Sector"] = sector_name

    #Building value score
    pe = sector_fund["PE"]
    sector_fund["value_z"] = -(pe - pe.mean()) / pe.std()

    sector_fund["value_rank"] = sector_fund["PE"].rank(
        ascending=True, 
        method="first"
    )

    #Sort by cheapest
    sector_fund = sector_fund.sort_values("value_rank")

    return sector_fund


# Run Test

def main():
    sector_name = "Financials"
    value_df = build_value_signal(sector_name)

    print(f"\n=== value signal for sector: {sector_name} ===")
    print(value_df.head(20))
    print("\nTotal names in sector: ", len(value_df))

    out_path = os.path.join(base_dir, "value_signal.parquet")
    value_df.to_parquet(out_path)
    print("\nSaved:", out_path)


if __name__ == "__main__":
    main()