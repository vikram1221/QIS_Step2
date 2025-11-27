import pandas as pd
import os

base_dir = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2"
panels_dir = os.path.join(base_dir, "panels")
close_path = os.path.join(panels_dir, "close_panel.parquet")
returns_path = os.path.join(panels_dir, "returns _panel.parquet")

def build_momentum_signal(skip=21, lookback=252):
    """
    Standard 12m-1m momentum factor.
    skip: days to skip (1 month)
    lookback: 12 months (252 days)
    """
    close = pd.read_parquet(close_path).sort_index()
    close = close.apply(pd.to_numeric, errors="coerce")
    mom = close.shift(skip) / close.shift(lookback) - 1
    mom = mom.iloc[lookback:]
    mom_z = mom.sub(mom.mean(axis=1), axis=0).div(mom.std(axis=1), axis=0)
    mom_z = pd.DataFrame(mom_z, index=mom.index, columns=mom.columns)

    return mom, mom_z

def main():
    mom, mom_z = build_momentum_signal()
    print("\n=== Momentum Z-score (first 5 rows) ===")
    print(mom_z.head())

    out_path = os.path.join(base_dir, "momentum_signal.parquet")
    mom_z.to_parquet(out_path)
    print("\nSaved momentum signal to: ", out_path)

if __name__ == "__main__":
    main()
