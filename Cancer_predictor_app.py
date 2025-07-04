import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit UI
st.set_page_config(page_title="Cancer Prediction App")
st.title("🔬 Cancer Prediction App")
st.markdown("Enter 31 comma-separated  features to predict if it's **Cancer** or **Not Cancer**.")

# Input field
user_input = st.text_input("Enter features (comma-separated):")

if st.button("Predict"):
    try:
        # Convert input string to float list
        feature_list = user_input.split(',')
        np_features = np.asarray(feature_list, dtype=np.float32).reshape(1, -1)

        # Make prediction
        prediction = model.predict(np_features)
        output = "🛑 Cancer Detected" if prediction[0] == 1 else "✅ No Cancer Detected"
        st.success(output)
    except:
        st.error("❌ Invalid input! Please enter only comma-separated numbers.")