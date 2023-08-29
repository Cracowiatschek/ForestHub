import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd
from engine.change_display_navbar import change_active_tab as cat

external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css']
# cross with Materialize CSS

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)  # utworzenie instancji

logo_path = 'assets/logo.png'

app.layout = html.Div([
    html.Div([
        dcc.Location(
            id='url',
            refresh=False
        ),
        html.Nav(
            className='nav-wrapper teal lighten-3',
            children=[
                html.A(
                    className='brand-logo',
                    children=html.Img(
                            src=logo_path,
                            height='70px'
                    )
                ),
                html.A(
                    className='brand-logo',
                    children='ForestHub',
                    style={'marginLeft': '70px'}
                ),
                html.Ul(
                    id='nav-mobile',
                    className='right hide-on-med-and-down',
                    children=[
                        html.Li(children=dcc.Link(children='About project', href='/'), className='active'),
                        html.Li(children=dcc.Link(children='Docs', href='/docs')),
                        html.Li(children=dcc.Link(children='Model App', href='/app')),
                        html.Li(children=dcc.Link(children='Contact', href='/contact'))
                    ]
                )
            ]
        )
    ]),
    html.Div(id='page-content')
])


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_content(pathname):
    print(pathname)
    return f'Strona {pathname}'


@app.callback(
    Output('nav-mobile', 'children'),
    [Input('url', 'pathname')]
)
def change_display_navbar(pathname):
    result = cat(pathname=pathname)
    return result


if __name__ == '__main__':
    app.run_server(debug=True)
