# Making Different Portfolios, Backtesting and Visualising

This project builds the full data pipeline that powers the factor research. It downloads S&P 500 tickers and price history, constructs clean price and returns panels, processes fundamental data, and generates both momentum and value signals. These signals are then transformed into investable momentum, value, and multi-factor portfolios. The project also includes an optional interactive Dash dashboard for visualizing cumulative returns, long/short performance, Sharpe ratios, and drawdowns.


## Project Workflow — Run in This Exact Order

1. `csv_downloader.py`  
   → Downloads S&P 500 tickers

2. `downloader.py`  
   → Downloads raw OHLCV price data for all tickers

3. `build_all_panels.py`  
   → Builds price panels (close, open, high, low, volume)

4. `returns_panel.py`  
   → Computes daily returns panel

5. `fundamentals_builder.py`  
   → Cleans + prepares fundamentals

6. `value_factor_matrix.py`  
   → Builds value factor matrix (PE, PB, EV/EBITDA, etc.)

7. `momentum_signal.py`  
   → Generates momentum signals

8. `value_signal.py`  
   → Generates value signals

9. `factor_portfolio.py`  
   → Build momentum, value, and multi-factor portfolios  
   → Outputs: `momentum_portfolio.parquet`, `value_portfolio.parquet`, `multi_factor_portfolio.parquet`

10. `view_panels.py`  
    → Inspects any panel/parquet file

11. `app/quant_dashboard.py`  
    → Launches Dash dashboard to visualize portfolios
