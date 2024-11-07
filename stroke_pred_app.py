import pandas as pd
import pickle
import streamlit as st

# Load the model
with open('AdaBoost_classifier1.pkl', 'rb') as pickle_in:
    model = pickle.load(pickle_in)

# Define mappings for categorical variables
gender_mapping = {"Male": 1, "Female": 0}
hypertension_mapping = {"0": 0, "1": 1}
heart_disease_mapping = {"0": 0, "1": 1}
ever_married_mapping = {"No": 0, "Yes": 1}
work_type_mapping = {
    "Never Worked": 0,
    "Private": 1,
    "Self-employed": 2,
    "Govt_job": 3,
    "Children": 4
}
residence_type_mapping = {"Urban": 1, "Rural": 0}
smoking_status_mapping = {
    "Never smoked": 0,
    "Formerly smoked": 1,
    "Smokes": 2
}

# Define feature names used during training
feature_names = [
    "gender", "age", "hypertension", "heart_disease",
    "ever_married", "work_type", "Residence_type",
    "avg_glucose_level", "bmi", "smoking_status"
]

def prediction(gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status):   
    # Convert inputs to numerical values
    gender_num = gender_mapping[gender]
    hypertension_num = hypertension_mapping[hypertension]
    heart_disease_num = heart_disease_mapping[heart_disease]
    ever_married_num = ever_married_mapping[ever_married]
    work_type_num = work_type_mapping[work_type]
    residence_type_num = residence_type_mapping[Residence_type]
    smoking_status_num = smoking_status_mapping[smoking_status]

    # Prepare input data for prediction
    input_data = [[gender_num, age, hypertension_num, heart_disease_num, ever_married_num, work_type_num, residence_type_num, avg_glucose_level, bmi, smoking_status_num]]
    
    # Convert to DataFrame
    input_df = pd.DataFrame(input_data, columns=feature_names)

    # Make prediction
    prediction = model.predict(input_df)
    return prediction 

def main(): 
    st.title("Stroke Prediction Web App by SRIJA BASAK 21BCE3506") 

    html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Stroke Prediction ML Web App by SRIJA BASAK 21BCE3506</h1> 
    </div> 
    """
    st.markdown(html_temp, unsafe_allow_html=True) 

    # User inputs
    gender = st.selectbox("Gender", options=["Male", "Female"]) 
    age = st.number_input("Age", min_value=0) 
    hypertension = st.selectbox("Hypertension", options=["0", "1"]) 
    heart_disease = st.selectbox("Heart Disease", options=["0", "1"]) 
    ever_married = st.selectbox("Ever Married", options=["No", "Yes"]) 
    work_type = st.selectbox("Work Type", options=["Never Worked", "Private", "Self-employed", "Govt_job", "Children"]) 
    Residence_type = st.selectbox("Residence Type", options=["Urban", "Rural"]) 
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0) 
    bmi = st.number_input("BMI", min_value=0.0) 
    smoking_status = st.selectbox("Smoking Status", options=["Never smoked", "Formerly smoked", "Smokes"]) 

    result = "" 

    if st.button("Predict"):
        result = prediction(gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status)
        
        if result[0] == 1:  # Check the prediction output
            result_text = "Stroke predicted"
        else:
            result_text = "Stroke not predicted"
        
        st.success(f'The output is: {result_text}') 

if __name__ == '__main__': 
    main() 
