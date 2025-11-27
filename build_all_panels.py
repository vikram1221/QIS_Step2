import os
from panel_builder import load_parquet, extract_price_panel, basic_clean

# Load combined dataset
path = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2\all_prices.parquet"
df = load_parquet(path)

# Create panels directory
panels_dir = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2\panels"
os.makedirs(panels_dir, exist_ok=True)

# Extract panels
close_panel  = extract_price_panel(df, "Close")
open_panel   = extract_price_panel(df, "Open")
high_panel   = extract_price_panel(df, "High")
low_panel    = extract_price_panel(df, "Low")
volume_panel = extract_price_panel(df, "Volume")

# Clean panels (forward-fill, back-fill, sort)
close_panel_clean  = basic_clean(close_panel)
open_panel_clean   = basic_clean(open_panel)
high_panel_clean   = basic_clean(high_panel)
low_panel_clean    = basic_clean(low_panel)
volume_panel_clean = basic_clean(volume_panel)

# Save to parquet
close_panel_clean.to_parquet(os.path.join(panels_dir, "close_panel.parquet"))
open_panel_clean.to_parquet(os.path.join(panels_dir, "open_panel.parquet"))
high_panel_clean.to_parquet(os.path.join(panels_dir, "high_panel.parquet"))
low_panel_clean.to_parquet(os.path.join(panels_dir, "low_panel.parquet"))
volume_panel_clean.to_parquet(os.path.join(panels_dir, "volume_panel.parquet"))

print("...panels created for the dataset")
