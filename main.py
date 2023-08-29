import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd

external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css']
# cross with Materialize CSS

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)  # utworzenie instancji

app.layout = html.Div([
    html.Div([
        html.Nav(
            className='nav-wrapper',
            children=[
                html.Img(
                    className='responsive-img',
                    src='../logo.png'
                ),
                html.A(
                    className='brand-logo',
                    children=html.Img(
                        className='responsive-img',
                        src='assets/logo.png'
                    )
                )
            ]
        )
    ]),
    html.Div(id='page-content', children=html.Img(src='file://./images/logo.png'))
])

if __name__ == '__main__':
    app.run_server(debug=True)
