import pandas as pd
import numpy as np


#read csv and transform datetime column to pandas datetime format
def read_csv(file):
    df = pd.read_csv(file)
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

#change UTCOffset
def floatToTimedelta(offset):
    return pd.Timedelta("{:02d}:00:00".format(int(offset)))

def changeUTCOffsetHelper(row):
    return row.datetime + floatToTimedelta(row.UTCOffset)

def changeUTCOffset(df):
    df['datetime'] = df.apply(changeUTCOffset,axis=1)
    return df
#functions to nicely filter data


def get_region(df, region):
    return df.loc[(df['region']==region)]

def get_source_id(df, source_id):
    return df.loc[(df['source_id']==source_id)]

def get_sensor_name(df, sensor_name):
    return df.loc[(df['sensor_name']==sensor_name)]

def get_unique_regions(df):
    return df['region'].unique()

def get_unique_source_ids(df):
    return df['source_id'].unique()

def get_unique_sensor_names(df):
    return df['sensor_name'].unique()

def get_time_interval(df, start_date, end_date):
    return df[(df['datetime'] > start_date) & (df['datetime'] <= end_date)]

def get_available_time_interval(df):
    return (df['datetime'].min(), df['datetime'].max())

def sort_by_datetime(df):
    return df.sort_values(by=['datetime'])
