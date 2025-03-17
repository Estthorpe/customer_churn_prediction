import streamlit as st 
import requests
import json
#Set API URL 
API_URL = "http://127.0.0.1:5000/predict"


# Streamlit UI Layout
st.title("🔍 Customer Churn Prediction Dashboard")
st.write("Fill in customer details below to predict churn.")

# Input Fields for Customer Data
customerID = st.text_input("Customer ID", "7590-VHVEG")
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=1)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox("Payment Method", 
                             ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
MonthlyCharges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=500.0, value=29.85)
TotalCharges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=29.85)

# Create input dictionary
input_data = {
    "customerID": customerID,
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges
}


# Submit button
if st.button("🔍 Predict Churn"):
    try:
        # Send request to Flask API
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        # Display Results
        churn_prediction = result["churn_prediction"]
        churn_probability = result["churn_probability"]

        # Display Prediction Result
        st.subheader("📊 Prediction Result")
        if churn_prediction == 1:
            st.error(f"⚠️ Customer is likely to churn! (Probability: {churn_probability:.2%})")
        else:
            st.success(f"✅ Customer is NOT likely to churn. (Probability: {churn_probability:.2%})")

        # Show probability
        st.write(f"**Churn Probability:** {churn_probability:.2%}")

    except Exception as e:
        st.error(f"Error: {e}")