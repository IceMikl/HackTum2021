# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 03:13:40 2021

@author: ajava
"""

from fbprophet import Prophet
import pandas as pd
import numpy as np

def floatToTimedelta(offset):
    return pd.Timedelta("{:02d}:00:00".format(int(offset)))

def func(row):
    
    return row.datetime + floatToTimedelta(row.UTCOffset)

df=pd.read_csv(r'C:/Users/ajava/Desktop/hackatum/ZEISS_hacakatum_challenge_dataset.csv')
def get_region(df, region):
    return df.loc[(df['region']==region)]

df=get_region(df,"APAC")

def get_sensor_name(df, sensor_name):
    return df.loc[(df['sensor_name']==sensor_name)]

df=get_sensor_name(df,"LSM_HS_TECO_Temperature_Hot1")
#tst_LSM_HS_SensorCan81_Temperature_Room= df.loc[df['sensor_name'] == "LSM_SR_Peltier_Temperature_Cool2"]

df['datetime'] = pd.to_datetime(df['datetime'])
df['datetime'] = df.apply(func,axis=1)
#drop UTCOffset column because we don't need it anymore
df = df.drop('UTCOffset', 1)
df['datetime'] = df['datetime'].dt.tz_localize(None)
df=df[["datetime","sensor_value"]]
df=df.rename(columns={"datetime":"ds", "sensor_value": "y"})
m = Prophet()

#takes about ~20 mins to train, so only reportable
m.fit(df)

future = m.make_future_dataframe(periods=100)
future.tail()
forecast = m.predict(future)
fig=m.plot(forecast)