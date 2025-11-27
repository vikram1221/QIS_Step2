from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

def app_layout():

    return html.Div([

        html.H1("Quant Factor Dashboard", style={"textAlign": "center"}),

        dcc.Tabs(
            id="tabs",
            value="momentum",
            children=[
                dcc.Tab(label="Momentum", value="momentum"),
                dcc.Tab(label="Value", value="value"),
                dcc.Tab(label="Multi-Factor", value="multi")
            ]
        ),

        html.Div(id="tab-content") 
    ])

def momentum_layout():
    return html.Div([
        html.H2("Momentum Factor Dashboard"),

        html.Div([
            dcc.Graph(id="momentum_cumret", style={"width": "48%", "display": "inline-block"}),
            dcc.Graph(id="momentum_longshort", style={"width": "48%", "display": "inline-block"}),
        ]),

        html.Div([
            dcc.Graph(id="momentum_sharpe", style={"width": "48%", "display": "inline-block"}),
            dcc.Graph(id="momentum_drawdown", style={"width": "48%", "display": "inline-block"}),
        ])
    ])


def value_layout():
    return html.Div([
        html.H2("Value Factor Dashboard"),

        html.Div([
            dcc.Graph(id="value_cumret", style={"width": "48%", "display": "inline-block"}),
            dcc.Graph(id="value_longshort", style={"width": "48%", "display": "inline-block"}),
        ]),

        html.Div([
            dcc.Graph(id="value_sharpe", style={"width": "48%", "display": "inline-block"}),
            dcc.Graph(id="value_drawdown", style={"width": "48%", "display": "inline-block"}),
        ])
    ])


def multi_layout():
    return html.Div([
        html.H2("Multi-Factor Dashboard"),

        html.Div([
            dcc.Graph(id="multi_cumret", style={"width": "48%", "display": "inline-block"}),
            dcc.Graph(id="multi_longshort", style={"width": "48%", "display": "inline-block"}),
        ]),

        html.Div([
            dcc.Graph(id="multi_sharpe", style={"width": "48%", "display": "inline-block"}),
            dcc.Graph(id="multi_drawdown", style={"width": "48%", "display": "inline-block"}),
        ])
    ])


def register_callbacks(app):

    @app.callback(
        Output("tab-content", "children"),
        Input("tabs", "value")
    )
    def render_tab_content(selected):
        if selected == "momentum":
            return momentum_layout()
        elif selected == "value":
            return value_layout()
        elif selected == "multi":
            return multi_layout()
