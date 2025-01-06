import streamlit as st
from pickle import load
import numpy as np
import os

# Load the model
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../models/pass_or_fail_decision_tree_classifier_random_42.sav")

try:
    model = load(open(model_path, "rb"))
except FileNotFoundError:
    st.stop()

# Class labels
class_dict = {
    '0': 'Fail',
    '1': 'Pass'
}

# App title
st.title("Student Test Result Prediction")
st.write("Enter the required details to predict whether the student will pass or fail.")

# Input fields
val1 = st.number_input("Hours Studied (0 - 50 hours)", min_value=0.0, max_value=50.0, step=0.1)
val2 = st.number_input("Attendance (0 - 100%)", min_value=0.0, max_value=100.0, step=0.1)
val3 = st.number_input("Previous Score (0 - 100%)", min_value=0.0, max_value=100.0, step=0.1)
val4 = st.number_input("Tutoring Sessions (0 - 10 sessions)", min_value=0.0, max_value=10.0, step=0.1)

# Dropdowns for categorical inputs
parental_involvement = st.selectbox(
    "Parental Involvement",
    options=["High", "Medium", "Low"]
)
resources = st.selectbox(
    "Access to Resources",
    options=["High", "Medium", "Low"]
)

# Map dropdown inputs to one-hot encoding
val5, val6, val7 = (1, 0, 0) if parental_involvement == "High" else (0, 0, 1) if parental_involvement == "Medium" else (0, 1, 0)
val8, val9, val10 = (1, 0, 0) if resources == "High" else (0, 0, 1) if resources == "Medium" else (0, 1, 0)

# Predict button
if st.button("Predict"):
    try:
        # Prepare data for prediction
        data = np.array([[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]])
        prediction = str(model.predict(data)[0])
        pred_class = class_dict[prediction]
        st.success(f"Prediction: {pred_class}")
    except Exception as e:
        st.error(f"Error in prediction: {str(e)}")
