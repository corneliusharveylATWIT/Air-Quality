import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSV
df = pd.read_csv("air_pollution_history.csv", parse_dates=["datetime"])

# Sidebar Filters
st.sidebar.title("Filters")
selected_pollutant = st.sidebar.selectbox("Select Pollutant", ["pm2_5", "pm10", "o3", "no2", "so2", "co", "nh3", "no"])

# Title
st.title("Air Quality Dashboard – Boston")

# Time Series Chart
st.subheader(f"{selected_pollutant.upper()} Levels Over Time")
fig = px.line(df, x="datetime", y=selected_pollutant, title=f"{selected_pollutant.upper()} Over Time")
st.plotly_chart(fig)

# AQI Overview
st.subheader("Air Quality Index (AQI)")
aqi_chart = px.line(df, x="datetime", y="aqi", color_discrete_sequence=["green"], title="AQI Over Time")
st.plotly_chart(aqi_chart)

# Raw Data
with st.expander("Show Raw Data"):
    st.dataframe(df)
