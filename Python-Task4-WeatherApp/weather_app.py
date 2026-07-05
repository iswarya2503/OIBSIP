import requests

# Ask the user for the city name
city = input("Enter city name: ")

# Check if the input is empty
if city == "":
    print("City name cannot be empty!")
    exit()

# Replace with your own API key
api_key ="189b09edf27a3eab92c7939e7d32891e"

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature_c = data["main"]["temp"]
        temperature_f = (temperature_c * 9/5) + 32
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n------ Weather Report ------")
        print("City:", city.title())
        print("Temperature:", round(temperature_c, 2), "°C")
        print("Temperature:", round(temperature_f, 2), "°F")
        print("Humidity:", humidity, "%")
        print("Weather:", weather.title())
        print("Wind Speed:", wind_speed, "m/s")

    else:
        print("City not found. Please enter a valid city name.")

except requests.exceptions.RequestException:
    print("Unable to connect. Please check your internet connection.")