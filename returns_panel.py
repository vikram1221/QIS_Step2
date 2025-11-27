import pandas as pd
import os

#Path to price panel
panels_dir = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2\panels"
close_path = os.path.join(panels_dir, r"close_panel.parquet")
returns_path = os.path.join(panels_dir, r"returns_panel.parquet")

close = pd.read_parquet(close_path).sort_index()
close = close.apply(pd.to_numeric, errors="coerce")

returns = close.pct_change().iloc[1:]
returns.to_parquet(returns_path)

print("Saved: ", returns_path)
print("Shape: ", returns.shape)
print(returns.head())