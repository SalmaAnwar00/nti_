import streamlit as st
import pandas as pd
import joblib

# Load the trained model pipeline
model = joblib.load("model.pkl")

st.title("Diabetes Prediction App")
st.write("Enter the patient's information below to predict diabetes risk.")

# Input fields matching the model's expected features
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", min_value=0, max_value=120, value=30)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
smoking_history = st.selectbox(
    "Smoking History",
    ["never", "current", "former", "ever", "not current", "No Info"]
)
bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0)
HbA1c_level = st.number_input("HbA1c Level", min_value=0.0, max_value=20.0, value=5.5)
blood_glucose_level = st.number_input("Blood Glucose Level", min_value=0, max_value=500, value=100)

if st.button("Predict"):
    input_data = pd.DataFrame({
        "gender": [gender],
        "age": [age],
        "hypertension": [hypertension],
        "heart_disease": [heart_disease],
        "smoking_history": [smoking_history],
        "bmi": [bmi],
        "HbA1c_level": [HbA1c_level],
        "blood_glucose_level": [blood_glucose_level]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("The model predicts: Diabetic")
    else:
        st.success("The model predicts: Not Diabetic")