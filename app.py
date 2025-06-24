import streamlit as st
import requests

API_KEY = "447aab79d6a0357144bb5f1f56bc7287"  # 🔑 Replace this with your real key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get("cod") != 200:
        return "City not found or error occurred.", None, None

    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    return f"🌡️ Temp: {temp}°C\n🌥️ Condition: {desc}", temp, desc

def suggest_outfit(temp, description):
    suggestions = []

    if temp is None:
        return "No suggestion available."

    if temp < 10:
        suggestions.append("Wear a warm coat 🧥 and gloves 🧤")
    elif temp < 20:
        suggestions.append("Wear a light jacket 🧥")
    else:
        suggestions.append("T-shirt weather! 😎")

    if "rain" in description:
        suggestions.append("Don't forget an umbrella ☔")
    elif "clear" in description:
        suggestions.append("Perfect for a walk or jog! 🏃‍♂️")

    return " | ".join(suggestions)

# Streamlit UI
st.set_page_config(page_title="AI Weather Assistant")
st.title("☁️ AI-Powered Weather Assistant")
st.write("Enter your city to get real-time weather updates and clothing suggestions.")

city = st.text_input("City Name")

if city:
    weather_text, temp, desc = get_weather(city)
    if temp is None:
        st.error(weather_text)
    else:
        st.success(weather_text)
        st.info("🧠 AI Suggestion: " + suggest_outfit(temp, desc))

