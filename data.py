import requests
import json
import csv

# Step 1: Define your API URL
url = "https://api.weatherbit.io/v2.0/current/airquality?city=Boston&postal_code=02124&key=052396392e5145448e3e53ddc8722e0d"

# Step 2: Get the response
response = requests.get(url)
data = response.json()

# Step 3: Extract the data (usually under 'data' key)
if "data" in data and isinstance(data["data"], list):
    air_quality_data = data["data"][0]  # Get the first result

    # Step 4: Write to CSV
    with open("boston_air_quality.csv", mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=air_quality_data.keys())
        writer.writeheader()
        writer.writerow(air_quality_data)

    print("✅ CSV file 'boston_air_quality.csv' created successfully.")
else:
    print("❌ No valid air quality data found.")
