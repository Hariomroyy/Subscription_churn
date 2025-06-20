import joblib
import numpy as np
import pandas as pd
import streamlit as st
#'Age', 'Gender', 'MonthlyCharges', 'ContractType'
# Load the model
model = joblib.load('model1.pkl')
scaler = joblib.load('scaler.pkl')

# Define the Streamlit app
st.title('Ott Churn Prediction')

st.divider()

# Get user input
age= st.number_input('Age', min_value=10, max_value=100)
gender = st.selectbox('Gender', ['Male', 'Female'])
if gender == 'Male':
    gender = 1
else:
    gender = 0
monthy_charges= st.number_input('Monthly Charges', min_value=30, max_value=150)
contract_type = st.selectbox('Contract Type', ['Month-to-Month', 'One-Year', 'Two-Year'])
if contract_type == 'Month-to-Month':
    contract_type = 0
elif contract_type == 'One-Year':
    contract_type = 1
else:
    contract_type = 2

st.divider()



predictbutton=st.button('Predict')

# Make predictions
input_df = pd.DataFrame([{
    'Age': age,
    'Gender': gender,
    'MonthlyCharges': monthy_charges,
    'ContractType': contract_type
}])

input_scaled = scaler.transform(input_df)
prediction = model.predict(input_scaled)

# Display the prediction
if prediction == 0:
    st.write('Not churn')
else:
    st.write('Churn')

st.divider()

proba = model.predict_proba(input_scaled)
st.write("Prediction probability (class 0, class 1):", proba)
