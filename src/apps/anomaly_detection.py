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


df = da.read_csv("../resources/Zeiss/ZEISS_hacakatum_challenge_dataset.csv")
df['datetime'] = pd.to_datetime(df['datetime'])

#this operation takes 1 minutes, turn off for testing
changeUTCOffset = False
if changeUTCOffset:
    df = da.changeUTCOffset(df)


date_ranges_info = []


sensor_name_options = {}
source_id_options = []
for source_id in da.get_unique_source_ids(df):
    source_id_options.append({'label':source_id, 'value':source_id})

    sensor_names = []
    for sensor_name in da.get_unique_sensor_names(da.get_source_id(df, source_id)):
        sensor_names.append({'label':sensor_name, 'value':sensor_name})
    sensor_name_options[source_id] = sensor_names



layout = html.Div(id = 'parent', children = [
        html.H1(id = 'H1', children = 'Anomaly Detection', style = {'textAlign':'center',\
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

        html.H4(id = 'contamination_text_isolation', children = 'Contamination percentage (0 to 100)', style = {'textAlign':'left',\
                                            'marginTop':20,'marginBottom':20}),

        dbc.Input(id="contamination_isolation", type="number", min=0, max=100, step=1, value=5),


        html.H4(id = 'data_range_tolerance_text_isolation', children = 'Date range tolerance', style = {'textAlign':'left',\
                                            'marginTop':20,'marginBottom':20}),

        dbc.Input(id="date_ranges_tolerance_isolation", type="number", value=7),


        html.Div(
            [
                dbc.Button(
                    "Apply anomaly detection", id="button_isolation", className="me-2", n_clicks=0
                ),
                html.Span(id="example-output", style={"verticalAlign": "middle"}),
            ]
            , style = {'textAlign':'left', 'marginTop':20,'marginBottom':20}
        ),

        # html.Div(id='date_ranges_isolation'),
        # html.Div(
        # id='date_ranges_isolation',
        # children=date_ranges_info),
        dbc.ListGroup(
        id='date_ranges_isolation',
            children=date_ranges_info
        ),


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
        [Output(component_id='plot_isolation', component_property= 'figure'),
        Output('date_ranges_isolation', 'children')],
        [Input('button_isolation', 'n_clicks'),
        Input(component_id='source_id_isolation', component_property= 'value'),
        Input(component_id='sensor_name_isolation', component_property= 'value'),
        Input('date_picker_isolation', 'start_date'),
        Input('date_picker_isolation', 'end_date'),
        Input('contamination_isolation', 'value'),
        Input('date_ranges_tolerance_isolation', 'value'),]
    )
    def displayClick(nclicks, source_id, sensor_name, start_date, end_date, contamination_isolation, date_ranges_tolerance_isolation):
        if nclicks > 0:
            df_a = da.get_sensor_name(da.get_source_id(df, source_id),sensor_name)
            if not (start_date is None or end_date is None):
                df_a = da.get_time_interval(df_a, start_date, end_date)
            df_a = df_a.sort_values(by=['datetime'])

            x = np.array(df_a.sensor_value).reshape(-1, 1)
            clf=IsolationForest(n_estimators=100, max_samples='auto', contamination=float(contamination_isolation/100.0), max_features=1.0, bootstrap=False, n_jobs=-1, random_state=42, verbose=0)
            clf.fit(x)
            y_data = clf.predict(x)

            anomalies = []
            for i in range(len(y_data)):
                if y_data[i] < 0:
                    anomalies.append(i)

            date_range_tolerance = date_ranges_tolerance_isolation #in days

            date_ranges = [df_a.iloc[anomalies].datetime.iloc[0]]
            prev_date = df_a.iloc[anomalies].datetime.iloc[0]
            for date in df_a.iloc[anomalies].datetime:
                if pd.Timedelta(date - prev_date).days > date_range_tolerance:
                    date_ranges.append(prev_date)
                    date_ranges.append(date)
                prev_date = date

            date_ranges.append(df_a.iloc[anomalies].datetime.iloc[-1])

            # output_string = ""
            date_ranges_info = [dbc.ListGroupItem("Anomalies occured in the following periods", active=True)]
            for i in range(0, len(date_ranges), 2):
                date_ranges_info.append(dbc.ListGroupItem("from {} till {}".format(date_ranges[i].strftime('%Y-%m-%d %H:%M'), date_ranges[i+1].strftime('%Y-%m-%d %H:%M'))))
                # date_ranges_info.append(html.Br())

            y_data[y_data==-1] = 0
            y_data = np.array(y_data, dtype=bool)
            fig = px.scatter(df_a, x="datetime", y="sensor_value", color=y_data)

            return fig, date_ranges_info

        return None, date_ranges_info
