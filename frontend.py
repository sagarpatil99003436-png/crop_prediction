import streamlit as st
import pandas as pd
import pickle

# -----------------------------------
# Load trained model
# -----------------------------------
with open("bagging_model.pkl", "rb") as file:
    model = pickle.load(file)


# -----------------------------------
# Page configuration
# -----------------------------------
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)


# -----------------------------------
# Title
# -----------------------------------
st.title("🌱 Crop Recommendation System")

st.write(
    "Enter soil nutrients and environmental conditions "
    "to get the recommended crop."
)


# -----------------------------------
# User Inputs
# -----------------------------------
st.subheader("Soil Nutrients")

col1, col2, col3 = st.columns(3)

with col1:
    N = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        value=90.0
    )

with col2:
    P = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        value=42.0
    )

with col3:
    K = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        value=43.0
    )


# -----------------------------------
# Environmental Conditions
# -----------------------------------
st.subheader("Environmental Conditions")

temperature = st.number_input(
    "Temperature (°C)",
    value=20.87
)

humidity = st.number_input(
    "Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=82.0
)

ph = st.number_input(
    "Soil pH",
    min_value=0.0,
    max_value=14.0,
    value=6.50
)

rainfall = st.number_input(
    "Rainfall (mm)",
    min_value=0.0,
    value=202.93
)


# -----------------------------------
# Prediction
# -----------------------------------
if st.button("🌾 Recommend Crop", use_container_width=True):

    input_data = pd.DataFrame(
        [[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]],
        columns=[
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall"
        ]
    )

    prediction = model.predict(input_data)

    st.success(
        f"🌱 Recommended Crop: {prediction[0].title()}"
    )