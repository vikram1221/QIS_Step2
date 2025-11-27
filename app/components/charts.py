import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Computing cumulative returns
def cumret(series):
    return(1 + series).cumprod() - 1

def plot_cumulative_return(factor_df, title="Cumulative Return"):
    df = factor_df.copy()
    df["cumret"] = cumret(df["factor"])
    fig = px.line(df, y="cumret", title=title)
    fig.update_layout(template="plotly_dark")
    return fig

# Long vs Short performance
def plot_long_short(factor_df, title="Long vs Short"):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=factor_df.index, y=factor_df["long"], 
        name="Long", mode="lines"
    ))
    fig.add_trace(go.Scatter(
        x=factor_df.index, y=factor_df["short"], 
        name="Short", mode="lines"
    ))
    fig.update_layout(title=title, template="plotly_dark")
    return fig

# Rolling Sharpe (30-day)
def plot_rolling_sharpe(factor_df, window=30):
    ret = factor_df["factor"]
    sharpe = ret.rolling(window).mean() / ret.rolling(window).std()

    fig = px.line(sharpe, title=f"Rolling Sharpe ({window}-day)")
    fig.update_layout(template="plotly_dark")
    return fig

# Drawdown chart
def plot_drawdown(factor_df):
    cum = cumret(factor_df["factor"])
    peak = cum.cummax()
    drawdown = cum - peak

    fig = px.area(drawdown, title="Drawdowns", color_discrete_sequence=["red"])
    fig.update_layout(template="plotly_dark")
    return fig