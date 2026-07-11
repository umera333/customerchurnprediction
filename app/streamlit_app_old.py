import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Load Model
# ----------------------------
model = joblib.load("models/best_model.pkl")
model_columns = joblib.load("models/model_columns.pkl")

# ----------------------------
# Title
# ----------------------------
st.title("📊 Customer Churn Prediction System")

st.markdown("""
Predict whether a telecom customer is likely to churn using Machine Learning.
Enter the customer's details below and click **Predict**.
""")

st.divider()

# ----------------------------
# Customer Information
# ----------------------------
col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )

    phone = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

with col2:

    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=200.0,
        value=70.0
    )

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=1000.0
    )

# ----------------------------
# Predict Button
# ----------------------------
predict = st.button("🚀 Predict Churn")

# ----------------------------
# Prediction
# ----------------------------
if predict:

    input_data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "InternetService": internet,
        "Contract": contract,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    input_df = pd.DataFrame([input_data])

    # Convert categorical variables into dummy variables
    input_df = pd.get_dummies(input_df)

    # Add missing columns
    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Keep column order same as training
    input_df = input_df[model_columns]

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("❌ Customer is likely to Churn")
    else:
        st.success("✅ Customer is NOT likely to Churn")

        