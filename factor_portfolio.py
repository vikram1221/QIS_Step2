import pandas as pd
import numpy as np
import os
from sector_universe import SectorUniverse

#Paths

base_dir = r"C:\Users\vikra\OneDrive\Desktop\Python Trading Programs\QIS_Step_2"
panels_dir = os.path.join(base_dir, "panels")
returns_path = os.path.join(panels_dir, "returns_panel.parquet")

sp500_path = os.path.join(base_dir, "SP500.csv")

# Factor Portfolio Engine

def build_factor_portfolio(factor_df, quantile=0.2, sector_neutral=False):
    """
    factor_df: DataFrame (Date x Tickers) with factor values
    quantile: top/bottom quantile to long/short
    sector_neutral: if True, pick top/bottom within each sector
    """

    returns = pd.read_parquet(returns_path)
    
    common_idx = factor_df.index.intersection(returns.index)
    factor_df = factor_df.loc[common_idx]
    returns = returns.loc[common_idx, factor_df.columns]

    long_rets = []
    short_rets = []

    if sector_neutral:
        print("Running Sector-Neutral portfolio...")

        universe = SectorUniverse(sp500_path)

        for date in factor_df.index:
            daily_factor = factor_df.loc[date]
            daily_returns = returns.loc[date]

            long_bucket = []
            short_bucket = []

            #for each sector computing long/short 
            for sector in universe.get_all_sectors():
                tickers = universe.get_sector_tickers(sector)
                tickers = [t for t in tickers if t in factor_df.columns]

                if len(tickers) < 5:
                    continue

                sub_factor = daily_factor[tickers].dropna()

                if len(sub_factor) < 5:
                    continue

                cutoff = int(len(sub_factor) * quantile)
                top = sub_factor.nlargest(cutoff).index
                bot = sub_factor.nsmallest(cutoff).index

                long_bucket.extend(top)
                short_bucket.extend(bot)

            #Computing daily returns
            long_rets.append(daily_returns[long_bucket].mean())
            short_rets.append(daily_returns[short_bucket].mean())

    else:
        print("Running standard (non-neutral) factor portfolio...")

        for date in factor_df.index:
            daily_factor = factor_df.loc[date]
            daily_returns = returns.loc[date]

            daily_factor = daily_factor.dropna()
            cutoff = int(len(daily_factor) * quantile)

            long_tickers = daily_factor.nlargest(cutoff).index
            short_tickers = daily_factor.nsmallest(cutoff).index

            long_rets.append(daily_returns[long_tickers].mean())
            short_rets.append(daily_returns[short_tickers].mean())

    long_rets = pd.Series(long_rets, index=factor_df.index)
    short_rets = pd.Series(short_rets, index=factor_df.index)

    factor_ret = long_rets - short_rets

    out = pd.DataFrame({
        "long"      : long_rets, 
        "short"     : short_rets,
        "factor"    : factor_ret
    })

    return out


def main():

    mom_path = os.path.join(base_dir, "momentum_signal.parquet")
    value_path = os.path.join(base_dir, "value_signal.parquet")


    #Momentum Portfolio
    print("\nLoading momentum...")
    mom = pd.read_parquet(mom_path)

    print("Building momentum portfolio...")
    mom_portfolio = build_factor_portfolio(mom, quantile=0.2)

    out_path = os.path.join(base_dir, "momentum_portfolio.parquet")
    mom_portfolio.to_parquet(out_path)
    print("\nSaved", out_path)

    print(mom_portfolio.head())

    #Value Portfolio
    print("\nLoading value signal...")
    value = pd.read_parquet(os.path.join(base_dir, "value_factor.parquet"))

    print("Building value portfolio...")
    value_portfolio = build_factor_portfolio(value, quantile=0.2)

    value_out = os.path.join(base_dir, "value_portfolio.parquet")
    value_portfolio.to_parquet(value_out)
    print("\nSaved: ", value_out)

    print(value_portfolio.head())

    #Multi-Factor Portfolio
    print("\nBuilding Multi_Factor signal...")

    common_idx = mom.index.intersection(value.index)
    common_cols = mom.columns.intersection(value.columns)

    mom_aligned = mom.loc[common_idx, common_cols]
    val_aligned = value.loc[common_idx, common_cols]

    #Equal weight combine
    multi_factor = (mom_aligned + val_aligned) / 2

    print("Building Multi-Factor portfolio...")
    multi_portfolio = build_factor_portfolio(multi_factor, quantile=0.2)

    multi_out = os.path.join(base_dir, "multi_factor_portfolio.parquet")
    multi_portfolio.to_parquet(multi_out)

    print("\nSaved: ", multi_out)
    print(multi_portfolio.head())

if __name__ == "__main__":
    main()