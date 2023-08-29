import dash_core_components as dcc
import dash_html_components as html


def change_active_tab(pathname):
    if pathname == '/':
        return [
            html.Li(children=dcc.Link(children='About project', href='/'), className='active'),
            html.Li(children=dcc.Link(children='Docs', href='/docs')),
            html.Li(children=dcc.Link(children='Model App', href='/app')),
            html.Li(children=dcc.Link(children='Contact', href='/contact'))
        ]
    elif pathname == '/docs':
        return [
            html.Li(children=dcc.Link(children='About project', href='/')),
            html.Li(children=dcc.Link(children='Docs', href='/docs'), className='active'),
            html.Li(children=dcc.Link(children='Model App', href='/app')),
            html.Li(children=dcc.Link(children='Contact', href='/contact'))
        ]
    elif pathname == '/app':
        return [
            html.Li(children=dcc.Link(children='About project', href='/')),
            html.Li(children=dcc.Link(children='Docs', href='/docs')),
            html.Li(children=dcc.Link(children='Model App', href='/app'), className='active'),
            html.Li(children=dcc.Link(children='Contact', href='/contact'))
        ]
    elif pathname == '/contact':
        return [
            html.Li(children=dcc.Link(children='About project', href='/')),
            html.Li(children=dcc.Link(children='Docs', href='/docs')),
            html.Li(children=dcc.Link(children='Model App', href='/app')),
            html.Li(children=dcc.Link(children='Contact', href='/contact'), className='active')
        ]
    else:
        return [
            html.Li(children=dcc.Link(children='About project', href='/')),
            html.Li(children=dcc.Link(children='Docs', href='/docs')),
            html.Li(children=dcc.Link(children='Model App', href='/app')),
            html.Li(children=dcc.Link(children='Contact', href='/contact'))
        ]