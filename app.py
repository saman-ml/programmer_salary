import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load('xgb.joblib')
st.title('Salary Prediction in 2022')
st.write("""### We need some information to predict the salary""")

countries = (
    "United States of America",
    "Iran, Islamic Republic of...",
    "India",
    "United Kingdom of Great Britain and Northern Ireland",
    "Germany",
    "Canada",
    "Brazil",
    "France",
    "Spain",
    "Australia",
    "Netherlands",
    "Poland",
    "Italy",
    "Russian Federation",
    "Sweden",
    "Switzerland",
    "Israel",
    "Austria",
    "Portugal",
    "Denmark",
    "Turkey",
    "Belgium",
    "Norway",
    "Finland",
    "Greece",
    "Czech Republic",
    "New Zealand",
    "Mexico",
    "South Africa",
    "Pakistan",
    "Other"
)

education = (
    "Less than a Bachelors",
    "Bachelor’s degree",
    "Master’s degree"
)

country = st.selectbox("Country", countries)
education = st.selectbox("Education Level", education)
expericence = st.slider("Years of Experience", 0, 50, 3)

ok = st.button("Calculate Salary")
if ok:
    X_new_df = pd.DataFrame({'Country':[country], 'EdLevel':[education], 'YearsCodePro':[expericence]})
    salary = model.predict(X_new_df)
    
    st.subheader(f"The estimated salary is ${salary[0]:.2f}")