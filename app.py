import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Load Model, Scaler & Encoders
# -------------------------------
model = joblib.load("salary_model.pkl")
scaler = joblib.load("scaler.pkl")
 

# -------------------------------
# App Title
# -------------------------------
st.set_page_config(page_title="Employee Salary Prediction", page_icon="💼")

st.title("💼 Employee Salary Prediction")
st.write("Fill the employee details below to predict the salary.")

# -------------------------------
# User Inputs
# -------------------------------

age = st.number_input("Age", min_value=18, max_value=60, value=25)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

education = st.selectbox(
    "Education",
    ["Bachelor", "Diploma", "Master", "PhD"]
)

experience = st.number_input(
    "Experience (Years)",
    min_value=0,
    max_value=40,
    value=2
)

department = st.selectbox(
    "Department",
    ["HR", "IT", "Marketing", "Operations", "Sales"]
)

job_level = st.selectbox(
    "Job Level",
    ["Junior", "Lead", "Manager", "Mid", "Senior"]
)

performance = st.slider(
    "Performance Rating",
    1,
    5,
    3
)

certifications = st.number_input(
    "Certifications",
    min_value=0,
    max_value=20,
    value=2
)

overtime = st.number_input(
    "Overtime Hours",
    min_value=0,
    max_value=100,
    value=10
)

remote = st.selectbox(
    "Remote Work",
    ["Yes", "No"]
)

city = st.selectbox(
    "City",
    ["Chennai", "Delhi", "Hyderabad", "Mumbai"]
)

company_tenure = st.number_input(
    "Company Tenure",
    min_value=0,
    max_value=40,
    value=2
)

projects = st.number_input(
    "Projects Completed",
    min_value=0,
    max_value=50,
    value=5
)

skill = st.slider(
    "Skill Score",
    0,
    100,
    70
)

# -------------------------------
# Prediction
# -------------------------------
# Manual Encoding

gender_encoded = 1 if gender == "Male" else 0

education_map = {
    "Diploma": 0,
    "Master": 1,
    "Bachelor": 2,
    "PhD": 3
}
education_encoded = education_map[education]

department_map = {
    "Sales": 0,
    "Operations": 1,
    "IT": 2,
    "HR": 3,
    "Marketing": 4
}
department_encoded = department_map[department]

job_level_map = {
    "Junior": 0,
    "Lead": 1,
    "Senior": 2,
    "Manager": 3,
    "Mid": 4
}
job_level_encoded = job_level_map[job_level]

remote_encoded = 1 if remote == "Yes" else 0

city_map = {
    "Chennai": 0,
    "Delhi": 1,
    "Hyderabad": 2,
    "Mumbai": 3
}
city_encoded = city_map[city]
if st.button("Predict Salary"):

    # Encode categorical columns
     
 

    # Create DataFrame (same order as training)
    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender_encoded],
        "Education": [education_encoded],
        "Experience_Years": [experience],
        "Department": [department_encoded],
        "Job_Level": [job_level_encoded],
        "Performance_Rating": [performance],
        "Certifications": [certifications],
        "Overtime_Hours": [overtime],
        "Remote_Work": [remote_encoded],
        "City": [city_encoded],
        "Company_Tenure": [company_tenure],
        "Projects_Completed": [projects],
        "Skill_Score": [skill]
    })

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    # Show result
    st.success(f"💰 Predicted Salary: ₹ {prediction[0]:,.2f}")
