import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from apps import index
from apps import data_visualization
from apps import data_visualization2
from apps import isolation_forests
from apps import anomaly_detection

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Zeiss", className="display-4"),
        html.Hr(),
        html.P(
            "Select your app", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Visualize data", href="/data_visualization", active="exact"),
                dbc.NavLink("Visualize data2", href="/data_visualization2", active="exact"),
                dbc.NavLink("Isolation forests", href="/isolation_forests", active="exact"),
                dbc.NavLink("Anomaly detection", href="/anomaly_detection", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

data_visualization.get_callbacks(app)
data_visualization2.get_callbacks(app)
isolation_forests.get_callbacks(app)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return index.page
    elif pathname == "/data_visualization":
        return data_visualization.layout
    elif pathname == "/data_visualization2":
        return data_visualization2.layout
    elif pathname == "/isolation_forests":
        return isolation_forests.layout
    elif pathname == "/anomaly_detection":
        return anomaly_detection.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug = True, port = 8050)
