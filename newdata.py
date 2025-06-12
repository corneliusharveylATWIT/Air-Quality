import requests
import csv
from datetime import datetime
import streamlit as st

# Streamlit UI
st.title("Air Pollution Data Downloader")
lat = st.number_input("Latitude", value=42.361145)
lon = st.number_input("Longitude", value=-71.057083)
start = st.number_input("Start timestamp", value=1606223802)
end = st.number_input("End timestamp", value=1606482999)
appid = st.text_input("API Key", value="80c311869e14b7da6397db8ab0d8179c")

if st.button("Fetch and Save Data"):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={appid}"
    response = requests.get(url)
    data = response.json()

    rows = []
    for entry in data["list"]:
        row = {
            "timestamp": datetime.utcfromtimestamp(entry["dt"]).isoformat(),
            "aqi": entry["main"]["aqi"],
            "co": entry["components"]["co"],
            "no": entry["components"]["no"],
            "no2": entry["components"]["no2"],
            "o3": entry["components"]["o3"],
            "so2": entry["components"]["so2"],
            "pm2_5": entry["components"]["pm2_5"],
            "pm10": entry["components"]["pm10"],
            "nh3": entry["components"]["nh3"]
        }
        rows.append(row)

    # Save file
    filename = "air_pollution_data.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    st.success(f"CSV saved as {filename}")
