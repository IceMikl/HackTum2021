import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from data_access import data_access as da
import dash_bootstrap_components as dbc
import numpy as np
from prophet import Prophet
import plotly.graph_objects as go
from prophet.plot import plot_plotly, plot_components_plotly
from prophet.plot import add_changepoints_to_plot


df = da.read_csv("../resources/Zeiss/ZEISS_hacakatum_challenge_dataset.csv")
df['datetime'] = pd.to_datetime(df['datetime'])
df = df.sort_values(by=['datetime'])

#this operation takes 1 minutes, turn off for testing
changeUTCOffset = False
if changeUTCOffset:
    df = da.changeUTCOffset(df)




sensor_name_options = {}
source_id_options = []
for source_id in sorted(da.get_unique_source_ids(df)):
    source_id_options.append({'label':source_id, 'value':source_id})

    sensor_names = []
    for sensor_name in da.get_unique_sensor_names(da.get_source_id(df, source_id)):
        sensor_names.append({'label':sensor_name, 'value':sensor_name})
    sensor_name_options[source_id] = sensor_names



layout = html.Div(id = 'parent', children = [
        html.H1(id = 'H1', children = 'Time Series Analysis', style = {'textAlign':'center',\
                                                'marginTop':40,'marginBottom':40}),



        html.H4(id = 'source_id_text_ts', children = 'Source id', style = {'textAlign':'left',\
                                    'marginTop':20,'marginBottom':20}),
        dcc.Dropdown(
            id='source_id_ts',
            options = source_id_options
        ),

        html.H4(id = 'sensor_name_text_ts', children = 'Sensor name', style = {'textAlign':'left',\
                                    'marginTop':20,'marginBottom':20}),
        dcc.Dropdown(
            id='sensor_name_ts',
        ),


        html.H4(id = 'date_picker_text_ts', children = 'Date picker', style = {'textAlign':'left',\
                                    'marginTop':20,'marginBottom':20}),
        dcc.DatePickerRange(
            id = 'date_picker_ts',
            min_date_allowed=date(2018, 1, 1),
            start_date_placeholder_text="Start Period",
            end_date_placeholder_text="End Period",
            calendar_orientation='vertical',
        ),




        html.Div(
            [
                dbc.Button(
                    "Apply time series analysis", id="button_ts", className="me-2", n_clicks=0
                ),
                html.Span(id="example-output", style={"verticalAlign": "middle"}),
            ]
            , style = {'textAlign':'left', 'marginTop':20,'marginBottom':100}
        ),


        html.Div([
                html.H4(children='Prediction Graph'),

                dcc.Graph(
                    id='plot_ts_1',
                ),
        ]),
        html.Div([
                html.H4(children='Trends'),

                dcc.Graph(
                    id='plot_ts_2',
                ),
        ]),
        # html.Div([
        #         html.H4(children='third graph'),
        #
        #         dcc.Graph(
        #             id='plot_ts_3',
        #         ),
        # ]),

    ])



def get_callbacks(app):

    @app.callback(
        dash.dependencies.Output('sensor_name_ts', 'options'),
        [dash.dependencies.Input('source_id_ts', 'value')]
    )
    def update_sensor_name_dropdown(source_id):
        if source_id is None: return []
        return sensor_name_options[source_id]



    @app.callback(
        [Output(component_id='plot_ts_1', component_property= 'figure'),
        Output(component_id='plot_ts_2', component_property= 'figure'),],
        [Input('button_ts', 'n_clicks'),
        Input(component_id='source_id_ts', component_property= 'value'),
        Input(component_id='sensor_name_ts', component_property= 'value'),
        Input('date_picker_ts', 'start_date'),
        Input('date_picker_ts', 'end_date'),]
    )
    def displayClick(nclicks, source_id, sensor_name, start_date, end_date):
        if nclicks > 0:
            df_a = da.get_sensor_name(da.get_source_id(df, source_id),sensor_name)
            if not (start_date is None or end_date is None):
                df_a = da.get_time_interval(df_a, start_date, end_date)
            df_a = df_a.sort_values(by=['datetime'])

            fig1, fig2 = get_fbresult(df_a)

            return fig1, fig2

        return fig1, fig2


def func(row):
    return row.datetime + floatToTimedelta(row.UTCOffset)
def floatToTimedelta(offset):
    return pd.Timedelta("{:02d}:00:00".format(int(offset)))

def get_fbresult(df, predict_days:int=10, **kwargs):
    df['datetime'] = df.apply(func,axis=1)

    #drop UTCOffset column because we don't need it anymore
    df = df.drop('UTCOffset', 1)

    df['datetime'] = df['datetime'].dt.tz_localize(None)
    df=df[["datetime","sensor_value"]]
    df=df.rename(columns={"datetime":"ds", "sensor_value": "y"})
    m = Prophet()
    m.fit(df)

    future = m.make_future_dataframe(periods=predict_days) #predicting 50days
    future.tail()

    forecast = m.predict(future)
    fig1 = plot_plotly(m, forecast)
    fig2 = plot_components_plotly(m, forecast)

    # fig3 = add_changepoints_to_plot(fig2.gca(), m, forecast) #changepoints

    return fig1, fig2
