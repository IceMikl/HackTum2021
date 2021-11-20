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
from sklearn.ensemble import IsolationForest
import numpy as np


df = da.read_csv("~/Desktop/hackatum/ZEISS_hacakatum_challenge_dataset.csv")
df['datetime'] = pd.to_datetime(df['datetime'])

#this operation takes 1 minutes, turn off for testing
changeUTCOffset = False
if changeUTCOffset:
    df = da.changeUTCOffset(df)



sensor_name_options = {}
source_id_options = []
for source_id in da.get_unique_source_ids(df):
    source_id_options.append({'label':source_id, 'value':source_id})

    sensor_names = []
    for sensor_name in da.get_unique_sensor_names(da.get_source_id(df, source_id)):
        sensor_names.append({'label':sensor_name, 'value':sensor_name})
    sensor_name_options[source_id] = sensor_names




layout = html.Div(id = 'parent', children = [
        html.H1(id = 'H1', children = 'Interactive visualization', style = {'textAlign':'center',\
                                                'marginTop':40,'marginBottom':40}),



        html.H4(id = 'source_id_text_isolation', children = 'Source id', style = {'textAlign':'left',\
                                    'marginTop':20,'marginBottom':20}),
        dcc.Dropdown(
            id='source_id_isolation',
            options = source_id_options
        ),

        html.H4(id = 'sensor_name_text_isolation', children = 'Sensor name', style = {'textAlign':'left',\
                                    'marginTop':20,'marginBottom':20}),
        dcc.Dropdown(
            id='sensor_name_isolation',
        ),


        html.H4(id = 'date_picker_text_isolation', children = 'Date picker', style = {'textAlign':'left',\
                                    'marginTop':20,'marginBottom':20}),
        dcc.DatePickerRange(
            id = 'date_picker_isolation',
            min_date_allowed=date(2018, 1, 1),
            start_date_placeholder_text="Start Period",
            end_date_placeholder_text="End Period",
            calendar_orientation='vertical',
        ),

        html.Div(
            [
                dbc.Button(
                    "Apply anomaly detection", id="button_isolation", className="me-2", n_clicks=0
                ),
                html.Span(id="example-output", style={"verticalAlign": "middle"}),
            ]
            , style = {'textAlign':'left',\
                                        'marginTop':20,'marginBottom':20}
        ),

        html.Div(id='date_ranges_isolation'),


        dcc.Graph(id = 'plot_isolation')
    ])



def get_callbacks(app):

    @app.callback(
        dash.dependencies.Output('sensor_name_isolation', 'options'),
        [dash.dependencies.Input('source_id_isolation', 'value')]
    )
    def update_sensor_name_dropdown(source_id):
        return sensor_name_options[source_id]



    @app.callback(
        Output('date_ranges_isolation', 'children'),
        Input('button_isolation', 'n_clicks'),
        Input(component_id='source_id_isolation', component_property= 'value'),
        Input(component_id='sensor_name_isolation', component_property= 'value'),
        Input('date_picker_isolation', 'start_date'),
        Input('date_picker_isolation', 'end_date')
    )
    def displayClick(nclicks, source_id, sensor_name, start_date, end_date):
        if nclicks > 0:
            df_a = da.get_sensor_name(da.get_source_id(df, source_id),sensor_name)
            if not (start_date is None or end_date is None):
                df_a = da.get_time_interval(df_a, start_date, end_date)
            df_a = df_a.sort_values(by=['datetime'])

            x = np.array(df_a.sensor_value).reshape(-1, 1)
            clf=IsolationForest(n_estimators=100, max_samples='auto', contamination=float(.05), max_features=1.0, bootstrap=False, n_jobs=-1, random_state=42, verbose=0)
            clf.fit(x)
            y_data = clf.predict(x)

            anomalies = []
            for i in range(len(y_data)):
                if y_data[i] < 0:
                    anomalies.append(i)

            date_range_tolerance = 0.1 #in days

            date_ranges = [df_a.iloc[anomalies].datetime.iloc[0]]
            prev_date = df_a.iloc[anomalies].datetime.iloc[0]
            for date in df_a.iloc[anomalies].datetime:
                if pd.Timedelta(date - prev_date).days > date_range_tolerance:
                    date_ranges.append(prev_date)
                    date_ranges.append(date)
                prev_date = date

            date_ranges.append(df_a.iloc[anomalies].datetime.iloc[-1])

            output_string = ""
            output_string += "Anomalies occured in the following periods\n"
            for i in range(0, len(date_ranges), 2):
                output_string += "From:{} to:{}\n".format(date_ranges[i], date_ranges[i+1])
            return output_string

        return ""


    # @app.callback(Output(component_id='plot_isolation', component_property= 'figure'),
    #               [
    #               Input(component_id='source_id_isolation', component_property= 'value'),
    #               Input(component_id='sensor_name_isolation', component_property= 'value'),
    #               Input('date_picker_isolation', 'start_date'),
    #               Input('date_picker_isolation', 'end_date')
    #               ])
    #
    # def graph_update(region, source_id, sensor_name, start_date, end_date):
    #     print(start_date)
    #     print(end_date)
    #     #fig = px.scatter(tst_LSM_HS_SensorCan81_Temperature_Room, x="datetime", y="sensor_value")
    #     df_a = da.get_sensor_name(da.get_source_id(da.get_region(df, region), source_id),sensor_name)
    #     if not (start_date is None or end_date is None):
    #         df_a = da.get_time_interval(df_a, start_date, end_date)
    #     fig = px.scatter(df_a, x="datetime", y="sensor_value", color="region", symbol="region")
    #
    #    #fig = go.Figure([go.Scatter(x = tst_LSM_HS_SensorCan81_Temperature_Room['datetime'], y = tst_LSM_HS_SensorCan81_Temperature_Room['sensor_value'],\
    #    #                 line = dict(color = 'firebrick', width = 4))
    #    #                ])
    #
    #     fig.update_layout(title = 'Region:{} Source Id:{} Sensor Name:{} - change of temperature value over time'.format(region, source_id, sensor_name),
    #                       xaxis_title = 'Dates',
    #                       yaxis_title = 'Temp'
    #                       )
    #     return fig
