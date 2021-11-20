import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

layout = html.Div([
        html.H1(children='Time Series Analysis'),
])



"""
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 03:13:40 2021

@author: ajava
"""

from fbprophet import Prophet
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from prophet.plot import plot_plotly, plot_components_plotly
from dyplot.dygraphs import Dygraphs
from prophet.plot import add_changepoints_to_plot
import altair as alt


def floatToTimedelta(offset):
    return pd.Timedelta("{:02d}:00:00".format(int(offset)))

def func(row):

    return row.datetime + floatToTimedelta(row.UTCOffset)

# df=pd.read_csv(r'C:/Users/ajava/Desktop/hackatum/ZEISS_hacakatum_challenge_dataset.csv')
def get_region(df, region="DACH"):
    return df.loc[(df['region']==region)]

# df=get_region(df,"APAC")

def get_sensor_name(df, sensor_name):
    return df.loc[(df['sensor_name']==sensor_name)]

def get_time_interval(df, start_date, end_date):
    return df[(df['datetime'] > start_date) & (df['datetime'] <= end_date)]


def get_fbresult(region:str="DACH",sensor_name:str="LSM_SR_Peltier_Temperature_Hot2",time_start="2010",time_end="2022",predict_days:int=10, **kwargs):
    df=pd.read_csv(r'C:/Users/ajava/Desktop/hackatum/ZEISS_hacakatum_challenge_dataset.csv')
    df=get_region(df,region)
    df=get_sensor_name(df,sensor_name)
    df=get_time_interval(df,time_start,time_end)
    df['datetime'] = pd.to_datetime(df['datetime'])
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
    fig=m.plot(forecast)

    fig2 = m.plot_components(forecast) #components

    fig3 = add_changepoints_to_plot(fig2.gca(), m, forecast) #changepoints

    return [forecast,fig,fig2,fig3]

df=get_fbresult()
"""
