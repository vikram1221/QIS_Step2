import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from components.layouts import app_layout, register_callbacks


# Import local components
from components.charts import(
    plot_cumulative_return, plot_long_short, 
    plot_rolling_sharpe, plot_drawdown
)

# Load Data
base_path = os.path.dirname(os.path.abspath(__file__))

momentum = pd.read_parquet("momentum_portfolio.parquet")
value = pd.read_parquet("value_portfolio.parquet")
multi = pd.read_parquet("multi_factor_portfolio.parquet")

# Dash App
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.layout = app_layout()
register_callbacks(app)


# Callbacks for Momentum
@app.callback(
    Output("momentum_cumret", "figure"), 
    Output("momentum_longshort", "figure"),
    Output("momentum_sharpe", "figure"),
    Output("momentum_drawdown", "figure"),
    Input("tabs", "value")
)

def update_momentum(_):
    return(
        plot_cumulative_return(momentum, "Momentum -- Cumulative Return"),
        plot_long_short(momentum, "Momentum -- Long vs Short"),
        plot_rolling_sharpe(momentum),
        plot_drawdown(momentum)
    )


# Callbacks for Value
@app.callback(
    Output("value_cumret", "figure"), 
    Output("value_longshort", "figure"), 
    Output("value_sharpe", "figure"),
    Output("value_drawdown", "figure"), 
    Input("tabs", "value")
)

def update_value(_):
    return(
        plot_cumulative_return(value, "Value -- Cumulative Return"), 
        plot_long_short(value, "Value -- Long vs Short"), 
        plot_rolling_sharpe(value), 
        plot_drawdown(value)
    )


# Callbacks for Multi-Factor
@app.callback(
    Output("multi_cumret", "figure"),
    Output("multi_longshort", "figure"),
    Output("multi_sharpe", "figure"),
    Output("multi_drawdown", "figure"),
    Input("tabs", "value")
)

def update_multi(_):
    return (
        plot_cumulative_return(multi, "Multi-Factor -- Cumulative Return"),
        plot_long_short(multi, "Multi-Factor -- Long vs Short"),
        plot_rolling_sharpe(multi),
        plot_drawdown(multi)
    )


# Expose server for Render/Gunicorn
server = app.server

# Allow local running
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8050)

