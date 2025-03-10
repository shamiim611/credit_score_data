# import libraries
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import dash_bootstrap_components as dbc

#register this page as the home page
dash.register_page(__name__, path="/Exploration", name="Exploration")


#read in the data
df = pd.read_csv(r'C:\Users\HP\Documents\dashapp practice\credit_score_app\data\credit_score_data.xls')
df.drop(columns=['ID','Customer_ID','Name','SSN'],inplace= True)# drop PII columns

#function to generate a table
def generate_table(df,max_rows = 2):
    return html.Table([
        # Table Header
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])  # Create a header row with column names
        ),
        
        # Table Body
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns  # Fill table rows with data
            ]) for i in range(min(len(df), max_rows))  # Limit number of rows to max_rows
        ])
    ])



#page layout
layout = dbc.Container([
    
    #page title
    html.H3("Data Exploration"),
    
    #table showing the first first rows of data
    html.Div([
        html.H5(children = 'Table showing first few rows of the data'),generate_table(df)
        ]),
    html.H4('Distributions for Selected Variables'),

    # Row containing both radio items and their respective graphs
    dbc.Row([
        # Column for Feature 1 selection and graph
        dbc.Col([
            html.Label("Select Feature for Graph 1:"),
            dcc.RadioItems(
                options=[
                    {'label': 'Annual_Income', 'value': 'Annual_Income'},
                    {'label': 'Age', 'value': 'Age'},
                    {'label': 'Amount_invested_monthly', 'value': 'Amount_invested_monthly'},
                ],
                value='Annual_Income',
                id="feature-selector-1",
                inline=True
            ),
            dcc.Graph(id="credit-risk-chart-1")
        ], width=6),

        # Column for Feature 2 selection and graph
        dbc.Col([
            html.Label("Select Feature for Graph 2:"),
            dcc.RadioItems(
                options=[
                    {'label': 'Credit_Score', 'value': 'Credit_Score'},
                    {'label': 'Payment_of_Min_Amount', 'value': 'Payment_of_Min_Amount'},
                    {'label': 'Credit_Mix', 'value': 'Credit_Mix'},
                ],
                value='Credit_Score',
                id="feature-selector-2",
                inline=True
            ),
            dcc.Graph(id="credit-risk-chart-2")
        ], width=6)
    ],className="mb-4"),

    # Second row of graphs
    html.H4('How does income, savings & investment affect credit score'),
    dbc.Row([
        dbc.Col([
            html.Label("Select Feature for Graph 3:"),
            dcc.RadioItems(
                options=[
                    {'label': 'Annual_Income', 'value': 'Annual_Income'},
                    {'label': 'Monthly_Inhand_Salary', 'value': 'Monthly_Inhand_Salary'},
                    
                ],
                value='Annual_Income',
                id="feature-selector-3",
                inline=True
            ),
            dcc.Graph(id="credit-risk-chart-3")
        ], width=6),

        dbc.Col([
            html.Label("Select Feature for Graph 4:"),
            dcc.RadioItems(
                options=[
                    {'label': 'Amount_invested_monthly', 'value': 'Amount_invested_monthly'},
                    {'label': 'Monthly_Balance', 'value': 'Monthly_Balance'},
                    
                ],
                value='Amount_invested_monthly',
                id="feature-selector-4",
                inline=True
            ),
            dcc.Graph(id="credit-risk-chart-4")
        ], width=6)
    ], className="mb-4"), # Adds spacing below this row

     # Third row of graphs
    html.H4('Does the number of accounts and borrowing behaviour affect credit score'),
    dbc.Row([
        dbc.Col([
            html.Label("Select Feature for Graph 5:"),
            dcc.RadioItems(
                options=[
                    {'label': 'Num_Bank_Accounts', 'value': 'Num_Bank_Accounts'},
                    {'label': 'Num_Credit_Card', 'value': 'Num_Credit_Card'},
                    
                ],
                value='Num_Bank_Accounts',
                id="feature-selector-5",
                inline=True
            ),
            dcc.Graph(id="credit-risk-chart-5")
        ], width=6),

        dbc.Col([
            html.Label("Select Feature for Graph 6:"),
            dcc.RadioItems(
                options=[
                    {'label': 'Num_of_Loan', 'value': 'Num_of_Loan'},
                    {'label': 'Interest_Rate', 'value': 'Interest_Rate'},
                    
                ],
                value='Num_of_Loan',
                id="feature-selector-6",
                inline=True
            ),
            dcc.Graph(id="credit-risk-chart-6")
        ], width=6)
    ], className="mb-4"), # Adds spacing below this row

# fourth row of graphs
    html.H4('Does debt, credit utilisation and payment behaviour affect credit score'),
    dbc.Row([
        dbc.Col([
            html.Label("Select Feature for Graph 7:"),
            dcc.RadioItems(
                options=[
                    {'label': 'Outstanding_Debt', 'value': 'Outstanding_Debt'},
                    {'label': 'Credit_Utilization_Ratio', 'value': 'Credit_Utilization_Ratio'},
                    
                ],
                value='Outstanding_Debt',
                id="feature-selector-7",
                inline=True
            ),
            dcc.Graph(id="credit-risk-chart-7")
        ], width=6),

        dbc.Col([
            html.Label("Select Feature for Graph 8:"),
            dcc.RadioItems(
                options=[
                    {'label': 'Delay_from_due_date', 'value': 'Delay_from_due_date'},
                    {'label': 'Num_of_Delayed_Payment', 'value': 'Num_of_Delayed_Payment'},
                    
                ],
                value='Delay_from_due_date',
                id="feature-selector-8",
                inline=True
            ),
            dcc.Graph(id="credit-risk-chart-8")
        ], width=6)
    ], className="mb-4") # Adds spacing below this row


], fluid = True

)

# Callback to update both graphs independently
@callback(
    [Output("credit-risk-chart-1", "figure"),
     Output("credit-risk-chart-2", "figure")],
    [Input("feature-selector-1", "value"),
     Input("feature-selector-2", "value")]
)
def update_charts(feature1, feature2):
    fig1 = px.histogram(df,  x =feature1, nbins= 10,
                      title=f"The distribution of {feature1}")
    # Create a DataFrame for plotting
    class_counts = df[feature2].value_counts(normalize=True).reset_index()
    class_counts.columns = [feature2, 'Proportion']

    fig2 = px.bar(class_counts, x=feature2,y='Proportion',
                  color_discrete_sequence=px.colors.qualitative.Set2, title=f"Bar Plot of {feature2}")
    fig2.update_layout(yaxis=dict(title='Proportion', range=[0, 1]),  # Setting y-axis limits
                  xaxis_title=feature2)

    
    return fig1, fig2

# Callback to update both graphs independently
@callback(
    [Output("credit-risk-chart-3", "figure"),
     Output("credit-risk-chart-4", "figure")],
    [Input("feature-selector-3", "value"),
     Input("feature-selector-4", "value")]
)
def update_charts(feature3, feature4):
    fig3 = px.box(df, x = 'Credit_Score', y =feature3,color='Credit_Score',color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'},title=f"The boxplot of {feature3} color coded by credit score")
    fig3.update_traces(quartilemethod="exclusive")
    # Create next graph
    
    fig4 = px.box(df, x = 'Credit_Score', y =feature4,color='Credit_Score',color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'},title=f"The boxplot of {feature4} color coded by credit score")
    fig4.update_traces(quartilemethod="exclusive")

    
    return fig3, fig4

# Callback to update both graphs independently
@callback(
    [Output("credit-risk-chart-5", "figure"),
     Output("credit-risk-chart-6", "figure")],
    [Input("feature-selector-5", "value"),
     Input("feature-selector-6", "value")]
)
def update_charts(feature5, feature6):
    fig5 = px.box(df, x = 'Credit_Score', y =feature5,color='Credit_Score',color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'},title=f"The boxplot of {feature5} color coded by credit score")
    fig5.update_traces(quartilemethod="exclusive")
    # Create next graph
    
    fig6 = px.box(df, x = 'Credit_Score', y =feature6,color='Credit_Score',color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'},title=f"The boxplot of {feature6} color coded by credit score")
    fig6.update_traces(quartilemethod="exclusive")

    
    return fig5, fig6

# Callback to update both graphs independently
@callback(
    [Output("credit-risk-chart-7", "figure"),
     Output("credit-risk-chart-8", "figure")],
    [Input("feature-selector-7", "value"),
     Input("feature-selector-8", "value")]
)
def update_charts(feature7, feature8):
    fig7 = px.box(df, x = 'Credit_Score', y =feature7,color='Credit_Score',color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'},title=f"The boxplot of {feature7} color coded by credit score")
    fig7.update_traces(quartilemethod="exclusive")
    # Create next graph
    
    fig8 = px.box(df, x = 'Credit_Score', y =feature8,color='Credit_Score',color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'},title=f"The boxplot of {feature8} color coded by credit score")
    fig8.update_traces(quartilemethod="exclusive")

    
    return fig7, fig8




