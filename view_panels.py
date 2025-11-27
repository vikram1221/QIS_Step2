import pandas as pd
import os

BASE = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2\panels"

def view_panel(filename):
    path = os.path.join(BASE, filename)
    print(f"\n=== Viewing {path} ===")
    df = pd.read_parquet(path)
    print("\nShape:" , df.shape)
    print("\nColumns", df.columns[:10])
    print("\nFirst 10 rows:")
    print(df.head(10))
    print("\n------\n")

view_panel("close_panel.parquet")
view_panel("open_panel.parquet")
view_panel("high_panel.parquet")
view_panel("low_panel.parquet")
view_panel("volume_panel.parquet")