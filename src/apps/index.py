import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output



page = html.Div([

        html.H1(children=[html.Span('Welcome to '), html.Strong("Elegance", style={"color":"blue"}), html.Span(' dashboard')]),
        html.Div(children='''
        Select an app which you would like to use
        '''),

        html.Img( src="assets/index_image.jpg", style={'height':'20%', 'width':'60%','marginTop':40,  "display":"block", "margin-left":"auto", "margin-right":"auto"}),
        dcc.Link("Image by Vecteezy", href="https://www.vecteezy.com/free-vector/website-development", style={'font-size':10,  "margin-left":"auto", "margin-right":"auto"})
])
