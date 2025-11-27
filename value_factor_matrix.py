import pandas as pd
import os

base_dir = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2"
panels_dir = os.path.join(base_dir, "panels")

# Inputs
returns_path = os.path.join(panels_dir, "returns_panel.parquet")
value_path = os.path.join(base_dir, "value_signal.parquet")

# Output
out_path = os.path.join(base_dir, "value_factor.parquet")

def main():
    returns = pd.read_parquet(returns_path)
    value = pd.read_parquet(value_path)

    tickers = [t for t in value["Symbol"] if t in returns.columns]
    value = value[value["Symbol"].isin(tickers)]

    factor_series = value.set_index("Symbol")["value_z"]

    factor_matrix = pd.DataFrame(
        [factor_series] * len(returns.index), 
        index=returns.index
    )

    factor_matrix.to_parquet(out_path)
    print("Saved: ", out_path)
    print(factor_matrix.head())

if __name__ == "__main__":
    main()