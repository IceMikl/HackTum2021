import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

from data_access import data_access as da



df = da.read_csv("~/Desktop/hackatum/ZEISS_hacakatum_challenge_dataset.csv")
#this operation takes 1 minutes, turn off for testing
changeUTCOffset = False
if changeUTCOffset:
    df = da.changeUTCOffset(df)


region_options = []
source_id_options = {}
sensor_name_options = {}

for region in da.get_unique_regions(df):
    region_options.append({'label':region, 'value':region})

    source_ids = []
    for source_id in da.get_unique_source_ids(da.get_region(df, region)):
        source_ids.append({'label':source_id, 'value':source_id})

        sensor_names = []
        for sensor_name in da.get_unique_sensor_names(da.get_source_id(da.get_region(df, region), source_id)):
            sensor_names.append({'label':sensor_name, 'value':sensor_name})
        sensor_name_options[region+source_id] = sensor_names

    source_id_options[region] = source_ids



layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Interactive visualization', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),



        html.H4(id = 'region_text', children = 'Region', style = {'textAlign':'left',\
                                            'marginTop':20,'marginBottom':20}),
        dcc.Dropdown( id = 'region',
        options = region_options,
        value = region_options[0]),

        html.H4(id = 'source_id_text', children = 'Source id', style = {'textAlign':'left',\
                                    'marginTop':20,'marginBottom':20}),
        dcc.Dropdown(
            id='source_id',
        ),

        html.H4(id = 'sensor_name_text', children = 'Sensor name', style = {'textAlign':'left',\
                                    'marginTop':20,'marginBottom':20}),
        dcc.Dropdown(
            id='sensor_name',
        ),


        html.H4(id = 'date_picker_text', children = 'Date picker', style = {'textAlign':'left',\
                                    'marginTop':20,'marginBottom':20}),
        dcc.DatePickerRange(
            start_date_placeholder_text="Start Period",
            end_date_placeholder_text="End Period",
            calendar_orientation='vertical',
        ),

        dcc.Graph(id = 'plot')
    ])



def get_callbacks(app):

    @app.callback(
        dash.dependencies.Output('source_id', 'options'),
        [dash.dependencies.Input('region', 'value')]
    )
    def update_source_id_dropdown(region):
        return source_id_options[region]

    @app.callback(
        dash.dependencies.Output('sensor_name', 'options'),
        [dash.dependencies.Input('region', 'value'), dash.dependencies.Input('source_id', 'value'), ]
    )
    def update_sensor_name_dropdown(region, source_id):
        return sensor_name_options[region+source_id]


    @app.callback(Output(component_id='plot', component_property= 'figure'),
                  [Input(component_id='region', component_property= 'value'),
                  Input(component_id='source_id', component_property= 'value'),
                  Input(component_id='sensor_name', component_property= 'value'),
                  ])#add date
    def graph_update(region, source_id, sensor_name):
        #fig = px.scatter(tst_LSM_HS_SensorCan81_Temperature_Room, x="datetime", y="sensor_value")
        fig = px.scatter(da.get_sensor_name(da.get_source_id(da.get_region(df, region), source_id),sensor_name), x="datetime", y="sensor_value", color="region", symbol="region")

       #fig = go.Figure([go.Scatter(x = tst_LSM_HS_SensorCan81_Temperature_Room['datetime'], y = tst_LSM_HS_SensorCan81_Temperature_Room['sensor_value'],\
       #                 line = dict(color = 'firebrick', width = 4))
       #                ])

        fig.update_layout(title = 'Region:{} Source Id:{} Sensor Name:{} - change of temperature value over time'.format(region, source_id, sensor_name),
                          xaxis_title = 'Dates',
                          yaxis_title = 'Temp'
                          )
        return fig
