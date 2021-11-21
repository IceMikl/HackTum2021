import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc



layout = html.Div([
        html.H1(children = 'Hypotheses', style = {'textAlign':'center'}),


#####################################Hypothesis #1###########################################################
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


#####################################Hypothesis #2###########################################################
    html.Div([

        html.H5(children = 'Hypothesis #2', style = {'textAlign':'left',\
                                            'marginTop':55,'marginBottom':20, "border-bottom": "2px solid" }),

        dbc.Carousel(
        items=[
            {
                "key": "1",
                "src": "assets/Hypotheses/hypothesis_2.PNG",
                "header": "",
                "caption": "",
            },
       

        ],
        variant="dark",
        style = {'height':480, 'width':'100%', "display":"block", "margin-left":"auto", "margin-right":"auto"},),

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
                dbc.Card(dbc.CardBody("Correlation between different microscopes given the region and sensor? \n "
                                      "We see that")),
                id="collapse-2",
                is_open=False,
            ),
        ]
        )

]),


###################################Hypothesis #3#############################################################
    html.Div([

        html.H5(children = 'Hypothesis #3', style = {'textAlign':'left',\
                                            'marginTop':55,'marginBottom':20, "border-bottom": "2px solid" }),

        dbc.Carousel(
        items=[
            {
                "key": "1",
                "src": "assets/Hypotheses/hypothesis_3_1.PNG",
                "header": "",
                "caption": "",
            },
            {
                "key": "2",
                "src": "assets/Hypotheses/hypothesis_3_2.PNG",
                "header": "",
                "caption": "",
            },

        ],
        variant="dark",
        style = {'height':480, 'width':'100%',"display":"block", "margin-left":"auto", "margin-right":"auto"},),

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
                dbc.Card(dbc.CardBody("Hypothesis 3: Increase of \"LSM_HS_SensorCan81_Temperature_Room\" causes increase in \"LKM980_Main_Temperature_Outside\" \n" 
                                      "We see that the after the temperature in the room increased, there is "
                                      "also temperature increase on the LSM device outside. \n"
                                      "We can perform heating/cooling actions in advance to reduce temperature fluctuations.")),
                id="collapse-3",
                is_open=False,
            ),
        ]
        )

], style={'marginTop':40}),


#####################################Hypothesis #4###########################################################
    html.Div([

        html.H5(children = 'Hypothesis #4', style = {'textAlign':'left',\
                                            'marginTop':55,'marginBottom':20, "border-bottom": "2px solid" }),

        dbc.Carousel(
        items=[
            {
                "key": "1",
                "src": "assets/Hypotheses/big_temp_change.PNG",
                "header": "",
                "caption": "",
            },
            {
                "key": "2",
                "src": "assets/Hypotheses/big_temp_change.PNG",
                "header": "",
                "caption": "",
            },

        ],
        variant="dark",
        style = {'height':480, 'width':'100%', "display":"block", "margin-left":"auto", "margin-right":"auto"},),

        html.Div(
        [
            dbc.Button(
                "Read detailed description",
                id="collapse-button-4",
                className="mb-3",
                color="primary",
                n_clicks=0,
                style = { "display":"block", "margin-left":"auto", "margin-right":"auto"}
            ),
            dbc.Collapse(
                dbc.Card(dbc.CardBody("Hypothesis 4: \"Hot\" outliers are in summer, \"Cold\" outliers are in winter? "
                                      "So, less outliers are in spring and autumn?"
                                      "The Hypothesis 4 was not proved, if it would then it will be easier to"
                                      "detect anomalies.")),
                id="collapse-4",
                is_open=False,
            ),
        ]
        )

], style={'marginTop':40}),


#####################################Hypothesis #5###########################################################
    html.Div([

        html.H5(children = 'Hypothesis #5', style = {'textAlign':'left',\
                                            'marginTop':55,'marginBottom':20, "border-bottom": "2px solid" }),

        dbc.Carousel(
        items=[
            {
                "key": "1",
                "src": "assets/Hypotheses/big_temp_change.PNG",
                "header": "",
                "caption": "",
            },
            {
                "key": "2",
                "src": "assets/Hypotheses/big_temp_change.PNG",
                "header": "",
                "caption": "",
            },

        ],
        variant="dark",
        style = {'height':480, 'width':'100%', "display":"block", "margin-left":"auto", "margin-right":"auto"},),

        html.Div(
        [
            dbc.Button(
                "Read detailed description",
                id="collapse-button-5",
                className="mb-3",
                color="primary",
                n_clicks=0,
                style = { "display":"block", "margin-left":"auto", "margin-right":"auto"}
            ),
            dbc.Collapse(
                dbc.Card(dbc.CardBody("Hypothesis 5 (more a feature): In the case of anomaly suspicion,"
                                      " ask the system to measure the temperature again.")),
                id="collapse-5",
                is_open=False,
            ),
        ]
        )

], style={'marginTop':40}),


#####################################Hypothesis #6###########################################################
    html.Div([

        html.H5(children = 'Hypothesis #6', style = {'textAlign':'left',\
                                            'marginTop':55,'marginBottom':20, "border-bottom": "2px solid" }),

        dbc.Carousel(
        items=[
            {
                "key": "1",
                "src": "assets/Hypotheses/hypothesis_6_1_original.PNG",
                "header": "",
                "caption": "TEST",
            },
            {
                "key": "2",
                "src": "assets/Hypotheses/hypothesis_6_2_original.PNG",
                "header": "",
                "caption": "",
            },

        ],
        variant="dark",
        style = {'height':480, 'width':'100%', "display":"block", "margin-left":"auto", "margin-right":"auto"},),

        html.Div(
        [
            dbc.Button(
                "Read detailed description",
                id="collapse-button-4",
                className="mb-3",
                color="primary",
                n_clicks=0,
                style = { "display":"block", "margin-left":"auto", "margin-right":"auto"}
            ),
            dbc.Collapse(
                dbc.Card(dbc.CardBody("Hypothesis 6: Does the time of day (day, midday, afternoon, night) "
                                      "influence room temperature -> device temperature?"
                                      "The hypothesis was proved that for example at 18o'clock is the \"hottest\""
                                      "and temperature is the highest. After we know the surrounding temperature"
                                      "behaviour, we can adjust a heating/cooling in microscope.")),
                id="collapse-6",
                is_open=False,
            ),
        ]
        )

], style={'marginTop':40}),


#####################################Hypothesis #7###########################################################
    html.Div([

        html.H5(children = 'Hypothesis #7', style = {'textAlign':'left',\
                                            'marginTop':55,'marginBottom':20, "border-bottom": "2px solid" }),

        dbc.Carousel(
        items=[
            {
                "key": "1",
                "src": "assets/Hypotheses/hypothesis_7_1_original.PNG",
                "header": "",
                "caption": "",
            },
            {
                "key": "2",
                "src": "assets/Hypotheses/hypothesis_7_2_original.PNG",
                "header": "",
                "caption": "",
            },

        ],
        variant="dark",
        style = {'height':480, 'width':'100%', "display":"block", "margin-left":"auto", "margin-right":"auto"},),

        html.Div(
        [
            dbc.Button(
                "Read detailed description",
                id="collapse-button-7",
                className="mb-3",
                color="primary",
                n_clicks=0,
                style = { "display":"block", "margin-left":"auto", "margin-right":"auto"}
            ),
            dbc.Collapse(
                dbc.Card(dbc.CardBody("Hypothesis 7: ")),
                id="collapse-7",
                is_open=False,
            ),
        ]
        )

], style={'marginTop':40}),


#####################################Hypothesis #8###########################################################
    html.Div([

        html.H5(children = 'Hypothesis #8', style = {'textAlign':'left',\
                                            'marginTop':55,'marginBottom':20, "border-bottom": "2px solid" }),

        dbc.Carousel(
        items=[
            {
                "key": "1",
                "src": "assets/Hypotheses/hypothesis_8_1_original.PNG",
                "header": "",
                "caption": "",
            },
            {
                "key": "2",
                "src": "assets/Hypotheses/hypothesis_8_2_original.PNG",
                "header": "",
                "caption": "",
            },

        ],
        variant="dark",
        style = {'height':480, 'width':'100%', "display":"block", "margin-left":"auto", "margin-right":"auto"},),

        html.Div(
        [
            dbc.Button(
                "Read detailed description",
                id="collapse-button-8",
                className="mb-3",
                color="primary",
                n_clicks=0,
                style = { "display":"block", "margin-left":"auto", "margin-right":"auto"}
            ),
            dbc.Collapse(
                dbc.Card(dbc.CardBody("Hypothesis 8: ")),
                id="collapse-8",
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


    @app.callback(
    Output("collapse-4", "is_open"),
    [Input("collapse-button-4", "n_clicks")],
    [State("collapse-4", "is_open")],)
    def toggle_collapse_4(n, is_open):
        if n:
            return not is_open
        return is_open


    @app.callback(
    Output("collapse-5", "is_open"),
    [Input("collapse-button-5", "n_clicks")],
    [State("collapse-5", "is_open")],)
    def toggle_collapse_5(n, is_open):
        if n:
            return not is_open
        return is_open


    @app.callback(
    Output("collapse-6", "is_open"),
    [Input("collapse-button-6", "n_clicks")],
    [State("collapse-6", "is_open")],)
    def toggle_collapse_6(n, is_open):
        if n:
            return not is_open
        return is_open


    @app.callback(
    Output("collapse-7", "is_open"),
    [Input("collapse-button-7", "n_clicks")],
    [State("collapse-7", "is_open")],)
    def toggle_collapse_7(n, is_open):
        if n:
            return not is_open
        return is_open


    @app.callback(
    Output("collapse-8", "is_open"),
    [Input("collapse-button-8", "n_clicks")],
    [State("collapse-8", "is_open")],)
    def toggle_collapse_8(n, is_open):
        if n:
            return not is_open
        return is_open