import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output



page = html.Div([
        html.H1(children='Hello User'),
        html.Div(children='''
        Select what you want to do
        '''),
])
