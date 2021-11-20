# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 23:56:01 2021

@author: ajava
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 22:51:37 2021

@author: ajava
"""

import dash
#import dash_html_components as html
import plotly.graph_objects as go
#import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output

from dash import html
from dash import dcc


app = dash.Dash()

#df = px.data.stocks()
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv(r'../../resources/Zeiss/ZEISS_hacakatum_challenge_dataset.csv')
tst_LSM_HS_SensorCan81_Temperature_Room= df.loc[df['sensor_name'] == "LSM_HS_SensorCan81_Temperature_Room"]
#sensor_2_LSM_HS_OW85_Temperature_MPM=df.loc[df['sensor_name'] == "LSM_HS_OW85_Temperature_MPM"]
#sensor_3_LSM_HS_OW86_Temperature_ScannerAmp=df.loc[df['sensor_name'] == "LSM_HS_OW86_Temperature_ScannerAmp"]

sensors_list = df['sensor_name'].unique().tolist()
list_of_distinct_sensor_dfs=[]
for i,sensor in enumerate(sensors_list):
    sensor_name="sensor_{0}_{1}".format(i,sensor)
    new_df=df.loc[df['sensor_name']==sensor]
    list_of_distinct_sensor_dfs.append(new_df)
    


app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Interactive visualization', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        dcc.Dropdown( id = 'dropdown',
        options = [
            {'label': 'LSM_HS_TECO_Temperature_Hot1', 'value':'LSM_HS_OW85_Temperature_MPM'},
            {'label': 'LSM_HS_OW86_Temperature_ScannerAmp', 'value':'LSM_HS_OW86_Temperature_ScannerAmp'},
            {'label': 'LSM_HS_TECO_Temperature_Hot1', 'value':'LSM_HS_TECO_Temperature_Hot1'},
            {'label': 'MicoIFHS_Temperature', 'value':'MicoIFHS_Temperature'},
            {'label': 'LSM_HS_TECO_Temperature_Hot2', 'value':'LSM_HS_TECO_Temperature_Hot2'},
            {'label': 'LKM980_Main_Temperature_Inside', 'value':'LKM980_Main_Temperature_Inside'},
            {'label': 'LKM980_Main_Temperature_Outside', 'value':'LKM980_Main_Temperature_Outside'},
            {'label': 'LSM_HS_TECO_Temperature_Cool2', 'value':'LSM_HS_TECO_Temperature_Cool2'},
            {'label': 'LSM_HS_OW85_Temperature_Grabber', 'value':'LSM_HS_OW85_Temperature_Grabber'},
            {'label': 'LKM980_Main_Temperature_Heatsink_FbgLkm980', 'value':'LKM980_Main_Temperature_Heatsink_FbgLkm980'},
            {'label': 'LSM_HS_VM800_Temperature_Controller', 'value':'LSM_HS_VM800_Temperature_Controller'},
            {'label': 'MicoIFHS_Temperature', 'value':'LSM_HS_TECO_Temperature_Cool1'},
            {'label': 'LSM_HS_TECO_Temperature_Cool1', 'value':'LSM_HS_TECO_Temperature_Controller'},
            {'label': 'LKM980_Main_Temperature_FPGA', 'value':'LKM980_Main_Temperature_FPGA'},
            {'label': 'LSM_SR_Peltier_Temperature_Hot2', 'value':'LSM_SR_Peltier_Temperature_Hot2'},
            {'label': 'LSM_SR_Peltier_Temperature_Cool2', 'value':'LSM_SR_Peltier_Temperature_Cool2'},
            {'label': 'LSM_HS_PC_Temperature_Controller', 'value':'LSM_HS_PC_Temperature_Controller'},
            ],
        value = 'LSM_HS_TECO_Temperature_Hot1'),
        dcc.Graph(id = 'bar_plot')
    ])
    
@app.callback(Output(component_id='bar_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def graph_update(dropdown_value):
    print(dropdown_value)
    #fig = px.scatter(tst_LSM_HS_SensorCan81_Temperature_Room, x="datetime", y="sensor_value")
    fig = px.scatter(df.loc[df['sensor_name'] == "{}".format(dropdown_value)], x="datetime", y="sensor_value", color="region", symbol="region")

   #fig = go.Figure([go.Scatter(x = tst_LSM_HS_SensorCan81_Temperature_Room['datetime'], y = tst_LSM_HS_SensorCan81_Temperature_Room['sensor_value'],\
   #                 line = dict(color = 'firebrick', width = 4))
   #                ])
    
    fig.update_layout(title = 'Current Sensor:{} - change of temperature value over time'.format(dropdown_value),
                      xaxis_title = 'Dates',
                      yaxis_title = 'Temp'
                      )
    return fig  



if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug = True, port = 8050)
