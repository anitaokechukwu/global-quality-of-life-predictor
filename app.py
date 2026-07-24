import streamlit as st
import joblib 
import pandas as pd


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Quality of Life Predictor",
    page_icon="🌍",
    layout="centered"
)


# -----------------------------
# Load Trained Model
# -----------------------------

@st.cache_resource
def load_model():
    return joblib.load(
        "models/quality_of_life_model.pkl"
    )


model = load_model()


# -----------------------------
# Application Title
# -----------------------------

st.title("🌍 Global Quality of Life Predictor")

st.write(
    "Enter country-level indicators to predict the Quality of Life Value."
)


# -----------------------------
# Input Features
# -----------------------------

purchasing_power = st.number_input(
    "Purchasing Power Value",
    min_value=0.0,
    max_value=300.0,
    value=100.0
)

safety = st.number_input(
    "Safety Value",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

health_care = st.number_input(
    "Health Care Value",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

climate = st.number_input(
    "Climate Value",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

cost_of_living = st.number_input(
    "Cost of Living Value",
    min_value=0.0,
    max_value=200.0,
    value=50.0
)

property_price_to_income = st.number_input(
    "Property Price to Income Value",
    min_value=0.0,
    max_value=100.0,
    value=10.0
)

traffic_commute_time = st.number_input(
    "Traffic Commute Time Value",
    min_value=0.0,
    max_value=100.0,
    value=40.0
)

pollution = st.number_input(
    "Pollution Value",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)


# -----------------------------
# Create Prediction Data
# -----------------------------

input_data = pd.DataFrame({

    "Purchasing Power Value": [
        purchasing_power
    ],

    "Safety Value": [
        safety
    ],

    "Health Care Value": [
        health_care
    ],

    "Climate Value": [
        climate
    ],

    "Cost of Living Value": [
        cost_of_living
    ],

    "Property Price to Income Value": [
        property_price_to_income
    ],

    "Traffic Commute Time Value": [
        traffic_commute_time
    ],

    "Pollution Value": [
        pollution
    ]

})


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Quality of Life"):

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Quality of Life Value: {prediction[0]:.2f}"
    )
