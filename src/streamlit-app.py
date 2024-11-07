import streamlit as st
from pickle import load
import os

# Get the absolute path to the model file
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../models/pass_or_fail_decision_tree_classifier_random_42.sav")
model = load(open(model_path, "rb"))

class_dict = {
    '0': 'Fail',
    '1': 'Pass'
}

st.title("Student Test Prediction - Pass or Fail")


val1 = st.number_input('Hours Studied (0 - 50 hours)', min_value=0.0, format='%.2f')
val2 = st.number_input('Attendance (0 - 100%)', min_value=0.0, format='%.2f')
val3 = st.number_input('Previous Score (0 - 100%)', min_value=0.0, format='%.2f')
val4 = st.number_input('Tutoring Sessions (0 - 10 sessions)', min_value=0.0, format='%.2f')
val5 = st.number_input('Parental Involvment - High (1 = yes, 0 = no)', min_value=0.0, format='%.2f')
val6 = st.number_input('Parental Involvment - Low (1 = yes, 0 = no)', min_value=0.0, format='%.2f')
val7 = st.number_input('Parental Involvment - Medium (1 = yes, 0 = no)', min_value=0.0, format='%.2f')
val8 = st.number_input('Access to Resources - High (1 = yes, 0 = no)', min_value=0.0, format='%.2f')
val9 = st.number_input('Access to Resources - Low (1 = yes, 0 = no)', min_value=0.0, format='%.2f')
val10 = st.number_input('Access to Resources - Medium (1 = yes, 0 = no)', min_value=0.0, format='%.2f')

if st.button("Predict:"):
    # Prepare the input data as a 2D list (list of lists)
    data = [[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]]
    # Make the prediction 
    prediction = str(model.predict(data)[0])
    # Show the predicted class
    pred_class = class_dict[prediction]
    st.write(f'Prediction: {pred_class}')
