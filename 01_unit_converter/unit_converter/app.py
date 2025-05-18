import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🌐 Google-Style Unit Converter")

conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature", "Time"])

units = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet"],
    "Weight": ["Kilograms", "Grams", "Pounds"],
    "Temperature": ["Celsius", "Fahrenheit"],
    "Time": ["Seconds", "Minutes", "Hours"]
}

from_unit = st.selectbox("From Unit", units[conversion_type])
to_unit = st.selectbox("To Unit", units[conversion_type])
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

def convert(val, from_u, to_u, type_):
    if type_ == "Length":
        base = {"Meters": 1, "Kilometers": 1000, "Miles": 1609.34, "Feet": 0.3048}
    elif type_ == "Weight":
        base = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592}
    elif type_ == "Temperature":
        if from_u == to_u:
            return val
        elif from_u == "Celsius" and to_u == "Fahrenheit":
            return val * 9/5 + 32
        elif from_u == "Fahrenheit" and to_u == "Celsius":
            return (val - 32) * 5/9
        else:
            return val
    elif type_ == "Time":
        base = {"Seconds": 1, "Minutes": 60, "Hours": 3600}
    else:
        return val

    return val * base[from_u] / base[to_u]

if st.button("Convert"):
    result = convert(value, from_unit, to_unit, conversion_type)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
