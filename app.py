import streamlit as st
import numpy as np
import joblib
from pathlib import Path

# ------------------------------------------------------------------
# Absolute, bulletproof path resolution
# ------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "house_price_model.pkl"

# Debug (temporary – will confirm path)
# st.write("Looking for model at:", MODEL_PATH)
# st.write("Files here:", list(BASE_DIR.iterdir()))

model = joblib.load(MODEL_PATH)

# ------------------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------------------
st.set_page_config(page_title="USA Housing Price Predictor", layout="centered")

st.title("🏠 USA Housing Price Predictor")
st.write("Predict house prices based on area and housing features.")

avg_income = st.number_input(
    "Average Area Income", 10000.0, 150000.0, 70000.0
)
house_age = st.slider("Average House Age", 1.0, 10.0, 5.0)
rooms = st.slider("Average Number of Rooms", 3.0, 10.0, 6.0)
bedrooms = st.slider("Average Number of Bedrooms", 1.0, 6.0, 3.0)
population = st.number_input("Area Population", 100.0, 70000.0, 30000.0)

if st.button("Predict House Price"):
    features = np.array([[avg_income, house_age, rooms, bedrooms, population]])
    prediction = model.predict(features)[0]
    st.success(f"💰 Estimated House Price: ${prediction:,.2f}")
