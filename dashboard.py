import streamlit as st
import pandas as pd
import requests
from io import StringIO
import plotly.express as px

# Load data from API
@st.cache_data
def load_data():
    url = 'https://api.weatherbit.io/v2.0/current/airquality?city=Boston&postal_code=02124&key=052396392e5145448e3e53ddc8722e0d'
    response = requests.get(url)
    csv_data = StringIO(response.text)
    return pd.read_csv(csv_data)

df = load_data()

# Basic UI
st.title("CSV Dashboard")
st.write("Data from API")

# Data preview
st.dataframe(df.head())

# Filter
selected_col = st.selectbox("Select column to plot", df.select_dtypes(include='number').columns)

# Plot
fig = px.histogram(df, x=selected_col)
st.plotly_chart(fig)
