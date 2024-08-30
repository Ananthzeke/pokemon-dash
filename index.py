from dash import dcc, html
from dash.dependencies import Input, Output
from pages import home, explorer, comparison, team_builder

def layout():
    return html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])

def register_callbacks(app):
    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/explorer':
            return explorer.layout()
        elif pathname == '/comparison':
            return comparison.layout()
        elif pathname == '/team-builder':
            return team_builder.layout()
        else:
            return home.layout()
