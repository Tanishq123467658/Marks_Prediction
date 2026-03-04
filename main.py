import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load the trained XGBoost model
try:
    with open('xgboost_tuned_model.pkl', 'rb') as file:
        model = pickle.load(file)
    st.success("XGBoost model loaded successfully!")
except FileNotFoundError:
    st.error("Error: 'xgboost_tuned_model.pkl' not found. Please ensure the model file is in the same directory.")
    st.stop()
except Exception as e:
    st.error(f"Error loading XGBoost model: {e}")
    st.stop()

# Load the original dataset to fit LabelEncoders
try:
    original_df = pd.read_csv('Exam_Score_Prediction.csv')
    st.success("Original data 'Exam_Score_Prediction.csv' loaded successfully for encoder setup.")
except FileNotFoundError:
    st.error("Error: 'Exam_Score_Prediction.csv' not found. Please ensure the data file is in the same directory.")
    st.stop()
except Exception as e:
    st.error(f"Error loading original data: {e}")
    st.stop()

# --- Setup LabelEncoders for categorical features ---
# The categorical features used by the model based on the previous steps are:
# 'sleep_quality', 'study_method', 'facility_rating'

categorical_features_for_model = ['sleep_quality', 'study_method', 'facility_rating']
label_encoders = {}

for feature in categorical_features_for_model:
    le = LabelEncoder()
    le.fit(original_df[feature]) # Fit on the original string values
    label_encoders[feature] = le
    # st.write(f"Fitted LabelEncoder for {feature}: {le.classes_}") # For debugging/verification

# Streamlit App Title
st.title('Exam Score Prediction App')

st.markdown("""
This application predicts a student's exam score based on various input parameters.
""")

# --- User Input Features ---
st.header('Input Student Details')

# Numerical Inputs
study_hours = st.number_input('Study Hours (e.g., 5.0)', min_value=0.0, max_value=24.0, value=5.0, step=0.1)
class_attendance = st.number_input('Class Attendance (%) (e.g., 85.0)', min_value=0.0, max_value=100.0, value=85.0, step=0.1)
sleep_hours = st.number_input('Sleep Hours (e.g., 7.0)', min_value=0.0, max_value=24.0, value=7.0, step=0.1)

# Categorical Inputs
# Use the classes_ from the fitted LabelEncoder to populate selectbox options
sleep_quality_options = label_encoders['sleep_quality'].classes_
sleep_quality_selected = st.selectbox('Sleep Quality', sleep_quality_options, index=int(np.where(sleep_quality_options == 'average')[0][0]))

study_method_options = label_encoders['study_method'].classes_
study_method_selected = st.selectbox('Study Method', study_method_options, index=int(np.where(study_method_options == 'online videos')[0][0]))

facility_rating_options = label_encoders['facility_rating'].classes_
facility_rating_selected = st.selectbox('Facility Rating', facility_rating_options, index=int(np.where(facility_rating_options == 'medium')[0][0]))

# --- Prediction Button ---
if st.button('Predict Exam Score'):
    # Preprocess user input
    try:
        # Encode categorical features
        sleep_quality_encoded = label_encoders['sleep_quality'].transform([sleep_quality_selected])[0]
        study_method_encoded = label_encoders['study_method'].transform([study_method_selected])[0]
        facility_rating_encoded = label_encoders['facility_rating'].transform([facility_rating_selected])[0]

        # Create a DataFrame for the prediction
        # Ensure the order of columns matches the training data (X_train)
        input_data = pd.DataFrame([[
            study_hours,
            class_attendance,
            sleep_hours,
            sleep_quality_encoded,
            study_method_encoded,
            facility_rating_encoded
        ]], columns=[
            'study_hours',
            'class_attendance',
            'sleep_hours',
            'sleep_quality',
            'study_method',
            'facility_rating'
        ])

        # Make prediction
        prediction = model.predict(input_data)[0]
        
        # Clip prediction to be within 0 and 100
        prediction = np.clip(prediction, 0, 100)

        st.subheader('Predicted Exam Score:')
        st.success(f'{prediction:.2f}')

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

