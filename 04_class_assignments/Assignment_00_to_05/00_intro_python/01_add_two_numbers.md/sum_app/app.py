import streamlit as st

st.title("🔢 Add Two Numbers")

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

if st.button("Calculate Sum"):
    st.success(f"The total is: {num1 + num2}")
