from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
from data_access import data_access as da

df = da.read_csv("../resources/Zeiss/ZEISS_hacakatum_challenge_dataset.csv")
sensor_options = []
for sensor in da.get_unique_sensor_names(df):
    sensor_options.append({'label':sensor, 'value':sensor})





layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Interactive visualization', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        dcc.Dropdown( id = 'dropdown',
        options = sensor_options),
        dcc.Graph(id = 'bar_plot')
    ])


def get_callbacks(app):

    @app.callback(Output(component_id='bar_plot', component_property= 'figure'),
                  [Input(component_id='dropdown', component_property= 'value')])
    def graph_update(dropdown_value):
        fig = px.scatter(df.loc[df['sensor_name'] == "{}".format(dropdown_value)], x="datetime", y="sensor_value", color="source_id", symbol="region")

        fig.update_layout(title = 'Current Sensor:{} - change of temperature value over time'.format(dropdown_value),
                          xaxis_title = 'Dates',
                          yaxis_title = 'Temp'
                          )
        return fig
