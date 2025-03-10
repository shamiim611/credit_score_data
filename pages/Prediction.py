import pandas as pd
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input,register_page
import dash_bootstrap_components as dbc


#register this as the second page
dash.register_page(__name__, path="/Prediction", name="Prediction")

#read in the data
df = pd.read_csv(r'C:\Users\HP\Documents\dashapp practice\credit_score_app\data\credit_score_data.xls')
df.drop(columns=['ID','Customer_ID','Name','SSN'],inplace= True)# drop PII columns
# preprocessing of the type of loan column
#keeping less frequent categories as other
#chose 60 as a threhold because below 60 contained more than 3 loans taken
threshold = 60
top_categories = df['Type_of_Loan'].value_counts()[df['Type_of_Loan'].value_counts() >= threshold].index
df['Type_of_Loan'] = df['Type_of_Loan'].apply(lambda x: x if x in top_categories else 'multiple_loans')



# page layout

layout = html.Div([
    html.H3("Credit Score Prediction"),
    
    # Personal Information
    html.H4("Personal Information"),
    dcc.Input(id='Age', type='number', placeholder='Enter Age'),
    dcc.Dropdown(id='Occupation', options=[
        {'label': occupation,'value':occupation} for occupation in list(df['Occupation'].unique())
    ], placeholder='Select Occupation'),
    dcc.Input(id='Month', type='number', placeholder='Enter Month', min=1,max=8),
    
    # Income & Payment
    html.H4("Income & Payment"),
    dcc.Input(id='Annual_Income', type='number', placeholder='Enter Annual Income'),
    dcc.Input(id='Monthly_Inhand_Salary', type='number', placeholder='Enter Monthly Inhand Salary'),
    dcc.Input(id='Monthly_Balance', type='number', placeholder='Enter Monthly_Balance'),
    dcc.Input(id='Amount_invested_monthly', type='number', placeholder='Enter Amount_invested_monthly'),
    
    # Banking & Credit Accounts
    html.H4("Banking & Credit Accounts"),
    dcc.Input(id='Num_Bank_Accounts', type='number', placeholder='Number of Bank Accounts'),
    dcc.Input(id='Num_Credit_Card', type='number', placeholder='Number of Credit Cards'),
    
    # Loan & Debt History
    html.H4("Loan & Debt History"),
    dcc.Input(id='Num_of_Loan', type='number', placeholder='Number of Loans'),
    dcc.Dropdown(id='Type_of_Loan', options=[
        {'label': loan_type,'value':loan_type} for loan_type in list(df['Type_of_Loan'].unique())
    ], placeholder='Select Type of Loan'),
    dcc.Input(id='Outstanding_Debt', type='number', placeholder='Outstanding Debt'),
    dcc.Input(id='Total_EMI_per_month', type='number', placeholder='Total EMI per Month'),
    dcc.Input(id='Credit_History_Age', type='number', placeholder='Credit History Age (in years)'),
    
    # Credit Behavior & Payment Patterns
    html.H4("Credit Behavior & Payment Patterns"),
    dcc.Input(id='Interest_Rate', type='number', placeholder='Interest Rate'),
    dcc.Input(id='Delay_from_due_date', type='number', placeholder='Delay from Due Date'),
    dcc.Input(id='Num_of_Delayed_Payment', type='number', placeholder='Number of Delayed Payments'),
    dcc.Input(id='Changed_Credit_Limit', type='number', placeholder='Changed Credit Limit'),
    dcc.Input(id='Num_Credit_Inquiries', type='number', placeholder='Number of Credit Inquiries'),
    dcc.Input(id='Credit_Utilization_Ratio', type='number', placeholder='Credit Utilization Ratio'),
    dcc.RadioItems(id='Payment_of_Min_Amount', options=[
        {'label': 'Yes', 'value': 'Yes'},
        {'label': 'No', 'value': 'No'}
    ], labelStyle={'display': 'inline-block'}),
    dcc.Dropdown(id='Payment_Behaviour', options=[
        {'label': behavior,u'value':behavior} for behavior in list(df['Payment_Behaviour'].unique())],
          placeholder='Select Payment Behavior'),
    dcc.Dropdown(id='Credit_Mix', options=[
        {'label': mix,'value':mix} for mix in list(df['Credit_Mix'].unique())], placeholder='Select Credit Mix'),
    
    # Submit Button
    html.Button("Predict Credit Score", id='predict_button', n_clicks=0)
])

