import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load trained pipeline
model = pickle.load(open("credit_risk_model.pkl", "rb"))

st.set_page_config(page_title="Loan Risk Prediction", layout="centered")

st.title("🏦 Loan Default Risk Prediction")
st.write("Enter applicant details to predict loan default risk.")

# User Inputs
income = st.number_input("💰 Annual Income", min_value=0)
credit = st.number_input("🏦 Loan Amount", min_value=0)
annuity = st.number_input("📅 Monthly EMI", min_value=0)
age = st.number_input("🎂 Age (Years)", min_value=18)
employment = st.number_input("💼 Employment Years", min_value=0)
occupation = st.selectbox(
    "👔 Occupation Type",
    [
        "Laborers",
        "Core staff",
        "Sales staff",
        "IT staff",
        "Managers",
        "Drivers",
        "Accountants",
        "High skill tech staff",
        "Medicine staff",
        "Other"
    ])

# Feature Engineering
if income > 0:
    credit_to_income = credit / income
    annuity_to_income = annuity / income
else:
    credit_to_income = 0
    annuity_to_income = 0


input_data = pd.DataFrame([[
    occupation,
    credit,
    annuity,
    income,
    age,
    employment,
    credit_to_income,
    annuity_to_income
]], columns=[
    "OCCUPATION_TYPE",
    "AMT_CREDIT",
    "AMT_ANNUITY",
    "AMT_INCOME_TOTAL",
    "AGE_YEARS",
    "EMPLOYMENT_YEARS",
    "CREDIT_TO_INCOME",
    "ANNUITY_TO_INCOME"
])

# Prediction
if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("📊 Prediction Result")

    # Default Result
    if prediction == 1:
        default_status = "Default"
    else:
        default_status = "Not Default"

    st.write(f"🧾 Default Prediction: {default_status}")

    # Risk Level
    if probability < 0.3:
        risk_level = "🟢 Low Risk"
    elif probability < 0.7:
        risk_level = "🟡 Medium Risk"
    else:
        risk_level = "🔴 High Risk"

    st.write(f"⚠️ Risk Level: {risk_level}")

    # Probability
    st.write(f"📈 Default Probability: {round(probability * 100, 2)}%")