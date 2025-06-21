import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('models/model.pkl')

st.title("💳 Credit Card Fraud Detection App")

st.markdown("""
Enter 29 comma-separated values (V1 to V28 + Scaled Amount).
You can copy from a sample row in your dataset.
""")

input_data = st.text_input("Enter input values (comma-separated):")

if input_data:
    try:
        features = np.array([float(i) for i in input_data.split(',')]).reshape(1, -1)
        prediction = model.predict(features)
        
        if prediction[0] == 1:
            st.error("⚠️ Fraudulent Transaction Detected!")
        else:
            st.success("✅ Legitimate Transaction.")
    except:
        st.warning("❌ Invalid input format. Please enter 29 numerical values separated by commas.")
