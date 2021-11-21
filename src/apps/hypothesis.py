import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc



layout = html.Div([
        html.H1(children = 'Hypotheses', style = {'textAlign':'center'}),


################################################################################################
    html.Div([
        html.H5(children = 'Hypothesis #1', style = {'textAlign':'left',\
                                            'marginTop':55,'marginBottom':20, "border-bottom": "2px solid" }),

        dbc.Carousel(
        items=[
            {
                "key": "1",
                "src": "assets/plot_example.png",
                "header": "With header ",
                "caption": "and caption",
            },
            {
                "key": "2",
                "src": "assets/plot_example.png",
                "header": "With header only",
                "caption": "",
            },

        ],
        variant="dark",
        style = {'height':480, 'width':850, 'marginTop':50, 'marginBottom':200, "display":"block", "margin-left":"auto", "margin-right":"auto"},),

        html.Div(
        [
            dbc.Button(
                "Read detailed description",
                id="collapse-button-1",
                className="mb-3",
                color="primary",
                n_clicks=0,
                style = { "display":"block", "margin-left":"auto", "margin-right":"auto"}
            ),
            dbc.Collapse(
                dbc.Card(dbc.CardBody("Detailed description blalalalallalalalalalalallalalalalalallalalalalalallala")),
                id="collapse-1",
                is_open=False,
            ),
        ]
        )

]),
################################################################################################
    html.Div([

        html.H5(children = 'Hypothesis #2', style = {'textAlign':'left',\
                                            'marginTop':55,'marginBottom':20, "border-bottom": "2px solid" }),

        dbc.Carousel(
        items=[
            {
                "key": "1",
                "src": "assets/plot_example.png",
                "header": "With header ",
                "caption": "and caption",
            },
            {
                "key": "2",
                "src": "assets/plot_example.png",
                "header": "With header only",
                "caption": "",
            },

        ],
        variant="dark",
        style = {'height':480, 'width':850, 'marginTop':50, 'marginBottom':200, "display":"block", "margin-left":"auto", "margin-right":"auto"},),

        html.Div(
        [
            dbc.Button(
                "Read detailed description",
                id="collapse-button-2",
                className="mb-3",
                color="primary",
                n_clicks=0,
                style = { "display":"block", "margin-left":"auto", "margin-right":"auto"}
            ),
            dbc.Collapse(
                dbc.Card(dbc.CardBody("Detailed description blalalalallalalalalalalallalalalalalallalalalalalallala")),
                id="collapse-2",
                is_open=False,
            ),
        ]
        )

]),

################################################################################################
    html.Div([

        html.H5(children = 'Hypothesis #3', style = {'textAlign':'left',\
                                            'marginTop':55,'marginBottom':20, "border-bottom": "2px solid" }),

        dbc.Carousel(
        items=[
            {
                "key": "1",
                "src": "assets/plot_example.png",
                "header": "With header ",
                "caption": "and caption",
            },
            {
                "key": "2",
                "src": "assets/plot_example.png",
                "header": "With header only",
                "caption": "",
            },

        ],
        variant="dark",
        style = {'height':480, 'width':850, 'marginTop':50, 'marginBottom':200, "display":"block", "margin-left":"auto", "margin-right":"auto"},),

        html.Div(
        [
            dbc.Button(
                "Read detailed description",
                id="collapse-button-3",
                className="mb-3",
                color="primary",
                n_clicks=0,
                style = { "display":"block", "margin-left":"auto", "margin-right":"auto"}
            ),
            dbc.Collapse(
                dbc.Card(dbc.CardBody("Detailed description blalalalallalalalalalalallalalalalalallalalalalalallala")),
                id="collapse-3",
                is_open=False,
            ),
        ]
        )

], style={'marginTop':40}),
])
################################################################################################






def get_callbacks(app):

    @app.callback(
    Output("collapse-1", "is_open"),
    [Input("collapse-button-1", "n_clicks")],
    [State("collapse-1", "is_open")],)
    def toggle_collapse_1(n, is_open):
        if n:
            return not is_open
        return is_open

    @app.callback(
    Output("collapse-2", "is_open"),
    [Input("collapse-button-2", "n_clicks")],
    [State("collapse-2", "is_open")],)
    def toggle_collapse_2(n, is_open):
        if n:
            return not is_open
        return is_open

    @app.callback(
    Output("collapse-3", "is_open"),
    [Input("collapse-button-3", "n_clicks")],
    [State("collapse-3", "is_open")],)
    def toggle_collapse_3(n, is_open):
        if n:
            return not is_open
        return is_open
