import streamlit as st

# Apply colorful gradient styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(45deg, #ff0000, #ff7f00, #ffff00, #00ff00, #0000ff, #4b0082, #8b00ff);
        color: white;
    }
    .stApp {
        background: linear-gradient(45deg,rgb(172, 113, 113),rgb(184, 152, 121),rgb(189, 189, 133),rgb(95, 125, 95),rgb(212, 212, 227),rgb(197, 189, 203),rgb(204, 190, 216));
        color: black;
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(255, 0, 150, 0.4);
        border: 5px solid;
        border-image: linear-gradient(45deg, #ff0000, #ffff00, #0000ff, #8b00ff) 1;
    }
     
    .stSidebar {
        background: linear-gradient(45deg,rgb(172, 113, 113),rgb(184, 152, 121),rgb(189, 189, 133),rgb(95, 125, 95),rgb(212, 212, 227),rgb(197, 189, 203),rgb(204, 190, 216));
        color: white;
        padding: 20px;
        font-size:24px;
        border-radius: 15px;
        border: 4px solid;
        border-image: linear-gradient(45deg, #8b00ff, #4b0082, #0000ff, #00ff00, #ffff00, #ff7f00, #ff0000) 1;
    }
     
    h1 {
        text-align: center;
        font-size: 56px;
        color: black;
        text-shadow: 2px 2px 10px rgba(255, 255, 255, 0.6);
    }
   
    .stButton>button {
        background: linear-gradient(45deg, #ff7f00, #ffff00, #00ff00, #0000ff);
        color: black;
        font-size: 40px;
        font-weight: bold;
        padding: 12px 25px;
        border-radius: 15px;
        transition: 0.3s;
        box-shadow: 0px 10px 30px rgba(0, 201, 255, 0.5);
        border: 3px solid white;
    }
    .stButton>button:hover {
        transform: scale(1.08);
        background: linear-gradient(45deg,rgb(181, 156, 202),rgb(126, 108, 139),rgb(112, 112, 160));
        color: white;
        border: 3px solidrgb(248, 95, 95);
    }
    .result-box {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 25px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.6);
        border: 3px solid;
        border-image: linear-gradient(45deg, #ff0000, #ffff00, #00ff00, #0000ff) 1;
    }
    .footer {
        text-align: center;
        color: black;
        margin-top: 50px;
        font-size: 14px;
        font-weight: bold;
        text-shadow: 2px 2px 5px rgba(255, 255, 255, 0.6);
    }
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>🔄  Unit Converter</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# Sidebar menu

st.sidebar.markdown("<h1 style='text-align: center;  font-weight: bold; color: black;'>Choose Conversion Type</h1>", unsafe_allow_html=True)
conversion_type = st.sidebar.selectbox("", ["Length", "Weight", "Temperature"])

value = st.number_input("Enter Value", value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Pounds", "Ounces", "Grams", "Tons", "Stones"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Pounds", "Ounces", "Grams", "Tons", "Stones"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Functions
def length_convertor(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Inches": 39.37,
        "Feet": 3.28
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Pounds": 2.2046,
        "Ounces": 35.27,
        "Grams": 1000,
        "Tons": 0.0000220462,
        "Stones": 6.35029
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

if st.button("🎰 Convert Now!"):
    result = length_convertor(value, from_unit, to_unit) if conversion_type == "Length" else weight_convertor(value, from_unit, to_unit) if conversion_type == "Weight" else temperature_convertor(value, from_unit, to_unit)
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
    st.markdown("<div class='footer'>Created with 💖 by Nousheen Atif</div>", unsafe_allow_html=True)
    st.balloons()
