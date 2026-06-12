import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Customer Churn Predictor", page_icon="📊")

st.title("📊 Customer Churn Predictor")
st.write("Fill in the customer details below to predict whether they will churn.")

st.markdown("---")

# Input fields
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    phone_service = st.selectbox("Phone Service", ["No", "Yes"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])

with col2:
    device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
    payment_method = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 65.0)
    total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, 1500.0)

st.markdown("---")

# Encoding maps (matching LabelEncoder alphabetical order)
encode = {
    "gender": {"Female": 0, "Male": 1},
    "binary": {"No": 0, "Yes": 1},
    "multiple_lines": {"No": 0, "No phone service": 1, "Yes": 2},
    "internet_service": {"DSL": 0, "Fiber optic": 1, "No": 2},
    "three_option": {"No": 0, "No internet service": 1, "Yes": 2},
    "contract": {"Month-to-month": 0, "One year": 1, "Two year": 2},
    "payment_method": {
        "Bank transfer (automatic)": 0,
        "Credit card (automatic)": 1,
        "Electronic check": 2,
        "Mailed check": 3
    }
}

if st.button("🔍 Predict Churn"):
    # Build input array
    input_data = np.array([[
        encode["gender"][gender],
        encode["binary"][senior],
        encode["binary"][partner],
        encode["binary"][dependents],
        tenure,
        encode["binary"][phone_service],
        encode["multiple_lines"][multiple_lines],
        encode["internet_service"][internet_service],
        encode["three_option"][online_security],
        encode["three_option"][online_backup],
        encode["three_option"][device_protection],
        encode["three_option"][tech_support],
        encode["three_option"][streaming_tv],
        encode["three_option"][streaming_movies],
        encode["contract"][contract],
        encode["binary"][paperless_billing],
        encode["payment_method"][payment_method],
        monthly_charges,
        total_charges
    ]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.error(f"⚠️ This customer is likely to **CHURN**! (Confidence: {probability[1]*100:.1f}%)")
    else:
        st.success(f"✅ This customer is likely to **STAY**! (Confidence: {probability[0]*100:.1f}%)")

st.markdown("---")
st.caption("Built with Scikit-learn & Streamlit | Muhammed Shaheem")
