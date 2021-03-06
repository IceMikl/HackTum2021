import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from apps import index
from apps import interactive_visualization
from apps import group_visualization
from apps import anomaly_detection
from apps import time_series_analysis
from apps import hypothesis

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
        html.Img(src=app.get_asset_url('zeiss_logo.png'), style={'height':'20%', 'width':'70%', "display":"block", "margin-left":"auto", "margin-right":"auto"}),

        html.Hr(),
        # html.P([html.Strong("Elegance", style={"color":"blue"})]),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Interactive Visualization", href="/interactive_visualization", active="exact"),
                dbc.NavLink("Group Visualization", href="/group_visualization", active="exact"),
                dbc.NavLink("Anomaly Detection", href="/anomaly_detection", active="exact"),
                dbc.NavLink("Time Series Analysis", href="/time_series_analysis", active="exact"),
                dbc.NavLink("Hypotheses", href="/hypotheses", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

interactive_visualization.get_callbacks(app)
group_visualization.get_callbacks(app)
anomaly_detection.get_callbacks(app)
time_series_analysis.get_callbacks(app)
hypothesis.get_callbacks(app)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return index.page
    elif pathname == "/interactive_visualization":
        return interactive_visualization.layout
    elif pathname == "/group_visualization":
        return group_visualization.layout
    elif pathname == "/anomaly_detection":
        return anomaly_detection.layout
    elif pathname == "/time_series_analysis":
        return time_series_analysis.layout
    elif pathname == "/hypotheses":
        return hypothesis.layout

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.title = "ELEGANCE"
    app.run_server(host="0.0.0.0", debug=False, dev_tools_ui=False, dev_tools_props_check=False, port = 8050)
