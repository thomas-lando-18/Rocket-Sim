from dash import (
    Dash,
    dcc,
    html,
    Input,
    Output,
)

import plotly.express as px
import pandas as pd 

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Div(children=[
            html.H1("SpARC by OOT", className='header-title'),
            html.Div(
                children=html.Img(
                    src="assets/OOT_logo.png",
                    className="header-image",
                ),
                className='header-image-parent'
            )            
        ], className='header'),
        dcc.Tabs(children=[
            dcc.Tab(label='Simulator', value='sim'),
            dcc.Tab(label="Designer", value='design'),
        ])
    ]
, className='main')

if __name__ == '__main__':
    app.run(debug=True)