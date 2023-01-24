import streamlit as st

st.title("BMI Calculator")

height_cm = st.number_input("Height in cm", min_value=1, max_value=250)

weight_kg = st.number_input("Weight in kg", min_value=1, max_value=250)

bmi = weight_kg/(height_cm/100)**2

st.write("Your BMI is", bmi)

if bmi<18.5:
    st.write("やせ型です")
elif bmi<24.9:
    st.write("標準です")
elif bmi<29.9:
    st.write("肥満気味です")
else:
    st.write("肥満です")
