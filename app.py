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
    multiple_lines = st.selectbox("Multiple Lines", ["No", "No phone service", "Yes"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["No", "No internet service", "Yes"])
    online_backup = st.selectbox("Online Backup", ["No", "No internet service", "Yes"])

with col2:
    device_protection = st.selectbox("Device Protection", ["No", "No internet service", "Yes"])
    tech_support = st.selectbox("Tech Support", ["No", "No internet service", "Yes"])
    streaming_tv = st.selectbox("Streaming TV", ["No", "No internet service", "Yes"])
    streaming_movies = st.selectbox("Streaming Movies", ["No", "No internet service", "Yes"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
    payment_method = st.selectbox("Payment Method", [
        "Bank transfer (automatic)", "Credit card (automatic)",
        "Electronic check", "Mailed check"
    ])
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 65.0)
    total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, 1500.0)

st.markdown("---")

# Encoding maps (alphabetical LabelEncoder order)
encode_gender = {"Female": 0, "Male": 1}
encode_binary = {"No": 0, "Yes": 1}
encode_multiple_lines = {"No": 0, "No phone service": 1, "Yes": 2}
encode_internet = {"DSL": 0, "Fiber optic": 1, "No": 2}
encode_three = {"No": 0, "No internet service": 1, "Yes": 2}
encode_contract = {"Month-to-month": 0, "One year": 1, "Two year": 2}
encode_payment = {
    "Bank transfer (automatic)": 0,
    "Credit card (automatic)": 1,
    "Electronic check": 2,
    "Mailed check": 3
}

if st.button("🔍 Predict Churn"):
    input_data = np.array([[
        0,  # customerID encoded as 0 (dummy)
        encode_gender[gender],
        encode_binary[senior],
        encode_binary[partner],
        encode_binary[dependents],
        tenure,
        encode_binary[phone_service],
        encode_multiple_lines[multiple_lines],
        encode_internet[internet_service],
        encode_three[online_security],
        encode_three[online_backup],
        encode_three[device_protection],
        encode_three[tech_support],
        encode_three[streaming_tv],
        encode_three[streaming_movies],
        encode_contract[contract],
        encode_binary[paperless_billing],
        encode_payment[payment_method],
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

