import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1', type='text', value='Montréal'),
    dcc.Input(id='input-2', type='text', value='Canada'),
    html.Button(id='submit-button', children='Submit'),
    html.Div(id='div-1'),
])

@app.callback(
        Output(component_id='div-1', component_property='children'),
        Input(component_id='submit-button', component_property='n_clicks'),
        [State(component_id='input-1', component_property='value'),
         State(component_id='input-2', component_property='value')]
)
def update_output(n_clicks, input1, input2):
    return f'Input 1 is {input1} and Input 2 is {input2}'

if __name__ == "__main__":
    app.run_server(debug=True)
