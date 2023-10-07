import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='my-graph'),
    dcc.Slider(
        id='my-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])

@app.callback(
        Output(component_id='my-graph', component_property='figure'),
        [Input(component_id='my-slider', component_property='value')]
)
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(
        filtered_df,
        x='gdpPercap',
        y='lifeExp',
        size='pop',
        color='continent',
        hover_name='country',
        log_x=True,
        size_max=55
    )

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
