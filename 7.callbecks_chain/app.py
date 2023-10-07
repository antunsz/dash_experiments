import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'USA': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': ['Montréal', 'Toronto', 'Ottawa']
}

app.layout = html.Div([
    dcc.RadioItems(
        list(all_options.keys()),
        'USA',
        id='countries-radio'
    ),
    html.Hr(),
    dcc.RadioItems(id='cities-radio'),
    html.Hr(),
    html.Div(id='display-selected-values')
])

@app.callback(
        Output(component_id='cities-radio', component_property='options'),
        Input(component_id='countries-radio', component_property='value')
)
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]

@app.callback(
        Output(component_id='cities-radio', component_property='value'),
        Input(component_id='cities-radio', component_property='options')
)
def set_cities_value(available_options):
    return available_options[0]['value']

@app.callback(
        Output(component_id='display-selected-values', component_property='children'),
        Input(component_id='countries-radio', component_property='value'),
        Input(component_id='cities-radio', component_property='value')
)
def set_display_children(selected_country, selected_city):
    return f'You have selected {selected_country} and {selected_city}'

if __name__ == "__main__":
    app.run_server(debug=True)
