import streamlit as st
import pandas as pd
import joblib

st.write("### 10 year heartRate disease prediction")

col1, col2 = st.columns(2)

gender = col1.radio(" Choose your gender below", ('Male', 'Female'))

age = col1.number_input("Enter your age")

education = col2.selectbox("Highest academic qualification", ['High School', 'Graduate', 'Post Graduate', 'PhD'])

currentSmoker = col1.radio("Are you a smoker", ('Yes', 'No'))

cigsPerDay = col2.number_input("Number of cigarettes per day(If applicable)")

BPMeds = col1.radio("Are you under Blood Pressure Medication", ('Yes', 'No'))

prevalentStroke = col2.radio("Have you experienced a stroke before", ('Yes', 'No'))

prevalentHyp = col1.radio("Do you suffer from Hypertension", ('Yes', 'No'))

diabetes = col2.radio("Do you have diabetes", ('Yes', 'No'))

totChol = col1.number_input("Enter your cholesterol level")

sysBP = col2.number_input("Enter your systolic pressure")

diaBP = col1.number_input("Enter your diastolic pressure")

BMI = col2.number_input("Enter your Body Mass Index")

heartRate = col1.number_input("Enter your resting Heart Rate rate")

glucose = col2.number_input("Enter your glucose level")

df_predictions = pd.DataFrame([[gender, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]], 
columns = ['gender', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol','sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose'])

df_predictions['gender'] = df_predictions['gender'].apply(lambda x : 1 if x=='Male' else 0)

def transform(data):
    output=3
    if(data == 'High School'):
        output=0
    elif(data == 'Graduate'):
        output=1
    elif(data == 'Post Graduate'):
        output=2
    return(output)

df_predictions['education'] = df_predictions['education'].apply(transform)

df_predictions['currentSmoker'] = df_predictions['currentSmoker'].apply(lambda x : 1 if x == 'Yes' else 0)

df_predictions['cigsPerDay'] = df_predictions['cigsPerDay'].apply(lambda x : 1 if x == 'Yes' else 0)

df_predictions['BPMeds'] = df_predictions['BPMeds'].apply(lambda x : 1 if x=='Yes' else 0)

df_predictions['prevalentStroke'] = df_predictions['prevalentStroke'].apply(lambda x : 1 if x=='Yes' else 0)

df_predictions['prevalentHyp'] = df_predictions['prevalentHyp'].apply(lambda x : 1 if x=='Yes' else 0)

df_predictions['diabetes'] = df_predictions['diabetes'].apply(lambda x : 1 if x=='Yes' else 0)

model = joblib.load('HeartDisease_model.pkl')

prediction = model.predict(df_predictions)

if st.button("Predict"):
    if(prediction[0] == 1):
        st.write("YES. You may develop a heart disease in 10 years.")
    else:
        st.write("NO! You may not develop a heart disease in 10 years.")
