import streamlit as st

st.title("BMI 計算機（Streamlitデモ）")
st.write("これはテストです。")
height_cm = st.number_input("身長（cm）", min_value=100, max_value=250)

weight_kg = st.number_input("体重（kg）", min_value=20, max_value=250)

bmi = weight_kg / (height_cm / 100) ** 2

st.write("あなたのBMIは", bmi, "です。")

if bmi < 18.5:
    st.write("やせ型です")
elif bmi < 24.9:
    st.write("標準です")
elif bmi < 29.9:
    st.write("肥満気味です")
else:
    st.write("肥満です")


p = st.number_input("p")
n = st.number_input("n")

st.write("pのn乗は")
st.write(p**n)