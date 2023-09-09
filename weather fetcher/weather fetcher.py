import requests
import json 

API_KEY = "d8ebc97c54fc7428716f475e8496f0c7"

while True:
    city = input("what city's weather would you like to know?: ")
    # lat =  input("lattitude: ")
    # lon = input("longitide: ")

    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        # print(data)
        weather= (data["weather"])
        # print(weather)
        temperature = data["main"]["temp"]
        F = (int(temperature - 273.15) * 9/5 + 32)

        description = weather[0]["description"]

        print(f'The temperature is: {F}°F with {description}')  
    else: 
        print("error occured")
