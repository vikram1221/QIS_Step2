# Step 2: Making Different Portfolios, Backtesting and Visualising

Step 2 builds the full data pipeline that powers the factor research in this project. It downloads S&P 500 tickers and price history, constructs clean price and returns panels, processes fundamental data, and generates both momentum and value signals. These signals are then transformed into investable momentum, value, and multi-factor portfolios, all saved as reproducible .parquet files. The step also includes an optional interactive Dash dashboard for visualizing cumulative returns, long/short performance, Sharpe ratios, and drawdowns.


## Step 2 Workflow — Run in This Exact Order

1. `csv_downloader.py`  
   → Download S&P 500 tickers

2. `downloader.py`  
   → Download raw OHLCV price data for all tickers

3. `build_all_panels.py`  
   → Build price panels (close, open, high, low, volume)

4. `returns_panel.py`  
   → Compute daily returns panel

5. `fundamentals_builder.py`  
   → Clean + prepare fundamentals

6. `value_factor_matrix.py`  
   → Build value factor matrix (PE, PB, EV/EBITDA, etc.)

7. `momentum_signal.py`  
   → Generate momentum signals

8. `value_signal.py`  
   → Generate value signals

9. `factor_portfolio.py`  
   → Build momentum, value, and multi-factor portfolios  
   → Outputs: `momentum_portfolio.parquet`, `value_portfolio.parquet`, `multi_factor_portfolio.parquet`

10. *(Optional)* `view_panels.py`  
    → Inspect any panel/parquet file

11. *(Optional)* `app/quant_dashboard.py`  
    → Launch Dash dashboard to visualize portfolios
