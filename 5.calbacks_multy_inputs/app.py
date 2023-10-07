import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

available_indicators = df['Indicator Name'].unique()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Fertility rate, total (births per woman)'
            ),
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
            
        ], style={'width': '49%', 'display': 'inline-block'}),
        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Fertility rate, total (births per woman)'
            ),
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )

        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='my-graph'),

    dcc.Slider(
        id='my-slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        value=df['Year'].min(),
        marks={str(year): str(year) for year in df['Year'].unique()},
        step=None
    )
])

@app.callback(
        Output(component_id='my-graph', component_property='figure'),
        [
            Input(component_id='xaxis-column', component_property='value'),
            Input(component_id='yaxis-column', component_property='value'),
            Input(component_id='xaxis-type', component_property='value'),
            Input(component_id='yaxis-type', component_property='value'),
            Input(component_id='my-slider', component_property='value')
        ]
)
def update_graph(xaxis_value, yaxis_value, xaxis_type, yaxis_type, year_value):
    dff = df[df.Year == year_value]

    fig = px.scatter(
        x=dff[dff['Indicator Name'] == xaxis_value]['Value'],
        y=dff[dff['Indicator Name'] == yaxis_value]['Value'],
        hover_name=dff[dff['Indicator Name'] == yaxis_value]['Country Name']
    )


    fig.update_layout(transition_duration=500, margin={'l': 40, 'b': 40, 't': 10, 'r': 10}, hovermode='closest')

    fig.update_xaxes(title=xaxis_value, type='linear' if xaxis_type == 'Linear' else 'log')
    fig.update_yaxes(title=yaxis_value, type='linear' if yaxis_type == 'Linear' else 'log')

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
