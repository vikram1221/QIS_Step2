import os
import pandas as pd

# === Locate folders ===
current_dir = os.path.dirname(os.path.abspath(__file__))

# project root: QIS_Step2/
project_root = os.path.dirname(current_dir)

# app folder (where quant_dashboard.py is)
app_folder = os.path.join(project_root, "app")

print("Saving PKL files to:", app_folder)

# === Load PARQUET files (from project root) ===
momentum = pd.read_parquet(os.path.join(project_root, "momentum_portfolio.parquet"))
value    = pd.read_parquet(os.path.join(project_root, "value_portfolio.parquet"))
multi    = pd.read_parquet(os.path.join(project_root, "multi_factor_portfolio.parquet"))

# === Save PKL files directly into /app ===
momentum.to_pickle(os.path.join(app_folder, "momentum_portfolio.pkl"))
value.to_pickle(os.path.join(app_folder, "value_portfolio.pkl"))
multi.to_pickle(os.path.join(app_folder, "multi_factor_portfolio.pkl"))

print("✔ Pickle files successfully written to /app folder!")
