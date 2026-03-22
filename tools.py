import requests

def get_weather(city: str):
    api_key = "YOUR_OPENWEATHER_API_KEY"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url).json()

    return {
        "city": city,
        "temperature": res["main"]["temp"],
        "condition": res["weather"][0]["description"]
    }
