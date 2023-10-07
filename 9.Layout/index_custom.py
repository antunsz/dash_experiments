import dash_bootstrap_components as dbc
from dash import html
import dash

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

card_content = [
        dbc.CardHeader('Card Header'),
        dbc.CardBody(
            [
                html.H5('Card Title', className='card-title'),
                html.P('This is some card content', className='card-text')
                ]
            )
        ]

app.layout = html.Div([
    dbc.Row([
        dbc.Col(dbc.Card(card_content, color='primary', inverse=True, style={'height':'100vh', 'margin':'10px'}), sm=4),
        dbc.Col([
            dbc.Row([
                dbc.Col(dbc.Card(card_content, color='primary', inverse=True, style={'margin-top':'10px'})),
                dbc.Col(dbc.Card(card_content, color='primary', inverse=True, style={'margin-top':'10px'}))
            ]),
            dbc.Row([
                dbc.Col(dbc.Card(card_content, color='primary', inverse=True, style={'margin-top':'10px'})), 
                dbc.Col(dbc.Card(card_content, color='primary', inverse=True, style={'margin-top':'10px'})), 
                dbc.Col(dbc.Card(card_content, color='primary', inverse=True, style={'margin-top':'10px'})), 
            ])
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
