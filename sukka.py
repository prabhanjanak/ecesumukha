import streamlit as st
import json

st.title("Mini Project by Sumukha Nadig and Tarun J")

# Load the JSON data
with open('weather.json', 'r') as f:
    weather_data = json.load(f)

# Create a list of cities for the selectbox
cities = [city['city'] for city in weather_data]

city = st.selectbox("Select city name:", cities)

if city:
    # Find the weather data for the selected city
    city_weather = next(item for item in weather_data if item['city'] == city)
    
    st.write(f"### Weather in {city}")
    st.write(f"**Temperature:** {city_weather['weather']['temperature']} °C")
    st.write(f"**Weather:** {city_weather['weather']['description']}")
    st.write(f"**Humidity:** {city_weather['weather']['humidity']}%")
    st.write(f"**Wind Speed:** {city_weather['weather']['wind_speed']} m/s")
else:
    st.write("Please select a city name.")
