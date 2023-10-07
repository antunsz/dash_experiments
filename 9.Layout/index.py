import dash_bootstrap_components as dbc
from dash import html
import dash

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.Div('Column'), style={'background':'#ff0000'}, md=6),
        dbc.Col(html.Div('Column'), style={'background':'#0ff000'}, md=3),
        dbc.Col(html.Div('Column'), style={'background':'#00ff00'}, md=3)
        ])
    ])

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
