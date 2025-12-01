# student_marks_app.py
import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("student_marks_predictor.pkl")

st.title("Student Marks Predictor")

name = st.text_input("Enter Student Name:")
hours = st.number_input("Enter Study Hours:", min_value=0.0, max_value=24.0, step=0.1)

if st.button("Predict Marks"):
    if not name.strip():
        st.warning("Please enter the student's name.")
    else:
        prediction = model.predict([[hours]])[0]
        st.success(f"{name}'s Predicted Marks is: {prediction:.2f}%")
