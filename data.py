import streamlit as st
import requests
import pandas as pd

st.title("Boston Air Quality Dashboard")

# Fetch data from API
url = "https://api.weatherbit.io/v2.0/current/airquality?city=Boston&postal_code=02124&key=052396392e5145448e3e53ddc8722e0d"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if "data" in data and isinstance(data["data"], list):
        air_quality_data = data["data"][0]

        # Convert dict to dataframe (1-row)
        df = pd.DataFrame([air_quality_data])

        st.write("### Current Air Quality Data for Boston")
        st.dataframe(df)

        # Example: show a few key metrics nicely
        st.metric("AQI (US EPA)", air_quality_data.get("aqius", "N/A"))
        st.metric("PM2.5 (µg/m3)", air_quality_data.get("pm25", "N/A"))
        st.metric("Ozone (ppb)", air_quality_data.get("o3", "N/A"))
    else:
        st.error("No valid air quality data found.")
else:
    st.error(f"Failed to fetch data from API. Status code: {response.status_code}")
