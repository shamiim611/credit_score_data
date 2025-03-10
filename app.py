#import libraries
import dash
from dash import Dash,html, dcc, page_registry, page_container
import dash_bootstrap_components as dbc


#instantiate app
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions= True,
                use_pages= True)

#manually import the pages
import pages.Exploration
import pages.Prediction

# Debugging: Print detected pages
print("Registered Pages:", dash.page_registry)

#layout
app.layout = html.Div([
    #framework layout
    #application title
    html.Div("Credit Score Prediction Dashboard",style={'fontSize':50, 'textAlign': 'center'}),
    html.Div([
        dcc.Link(page['name']+" | ", href= page['path'])
        for page in dash.page_registry.values()
    ]),
    html.Hr(),
    #Content of each page
    dash.page_container
])

#run app
if __name__ =='__main__':
    app.run_server(debug = True)