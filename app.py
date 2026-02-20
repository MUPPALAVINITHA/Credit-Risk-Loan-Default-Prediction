import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model (pipeline)
model = joblib.load("credit_risk_model.pkl")

st.set_page_config(page_title="Credit Risk Prediction", layout="centered")

st.title("Credit Risk Prediction App")
st.write("Predict whether a loan applicant is likely to default")
st.markdown("---")

# Upload CSV
uploaded_file = st.file_uploader("Upload Applicant Data (CSV)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data")
    st.dataframe(data.head())

    # --- FEATURE ENGINEERING ---
    # Only create if columns exist in uploaded data
    if 'DAYS_EMPLOYED' in data.columns:
        data['EMPLOYMENT_YEARS'] = -data['DAYS_EMPLOYED'] / 365
    if 'DAYS_BIRTH' in data.columns:
        data['AGE_YEARS'] = -data['DAYS_BIRTH'] / 365
    if 'AMT_CREDIT' in data.columns and 'AMT_INCOME_TOTAL' in data.columns:
        data['CREDIT_TO_INCOME'] = data['AMT_CREDIT'] / data['AMT_INCOME_TOTAL']
        data['ANNUITY_TO_INCOME'] = data['AMT_ANNUITY'] / data['AMT_INCOME_TOTAL']
        data['CREDIT_TERM'] = data['AMT_CREDIT'] / data['AMT_ANNUITY']

    # Fill missing values for engineered features if needed
    engineered_cols = ['EMPLOYMENT_YEARS', 'AGE_YEARS', 'CREDIT_TO_INCOME', 'ANNUITY_TO_INCOME', 'CREDIT_TERM']
    for col in engineered_cols:
        if col not in data.columns:
            data[col] = 0  # numeric fill
        else:
            data[col] = data[col].replace([np.inf, -np.inf], 0)
            data[col] = data[col].fillna(0)

    # --- ALIGN COLUMNS WITH MODEL ---
    required_cols = model.named_steps['preprocessor'].feature_names_in_

    # Add missing columns
    for col in required_cols:
        if col not in data.columns:
            if col.startswith("num__"):
                data[col] = 0
            elif col.startswith("cat__"):
                data[col] = "Unknown"

    # Reorder columns to match training
    data = data[required_cols]

    if st.button("Predict"):
        # Predict using full pipeline
        predictions = model.predict(data)
        probabilities = model.predict_proba(data)[:, 1]

        data["Default Prediction"] = predictions
        data["Risk Probability %"] = (probabilities * 100).round(2)

        st.write("### Prediction Results")
        st.dataframe(data.head())

        st.download_button(
            label="Download Results",
            data=data.to_csv(index=False),
            file_name="credit_risk_predictions.csv",
            mime="text/csv"
        )

