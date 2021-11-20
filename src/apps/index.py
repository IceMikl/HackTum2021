import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output



page = html.Div([
        html.H1(children='Welcome to dashboard'),
        html.Div(children='''
        Select an app which you would like to use
        '''),
])
