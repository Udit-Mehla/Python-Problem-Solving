import streamlit as st
import pandas as pd
import pickle

# 1. Load the saved model
with open('titanic_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🚢 Titanic Survival Predictor")
st.write("Enter your details to see if you would have survived the Titanic!")

# 2. Create input fields for the user
pclass = st.selectbox("Ticket Class", [1, 2, 3])
age = st.slider("Age", 0, 100, 25)
sex = st.selectbox("Sex", ["Male", "Female"])
fare = st.number_input("Ticket Fare", value=32.0)
family_size = st.number_input("Family Members Aboard", value=1)

# 3. Convert inputs to model format
sex_male = 1 if sex == "Male" else 0
# Simplified inputs for the demo
input_data = [[pclass, age, 0, 0, fare, family_size, sex_male, 0, 1]]

# 4. Make prediction
if st.button("Predict My Fate"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("You Survived! 🎉")
    else:
        st.error("You did not survive. 🌊")