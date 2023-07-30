import requests
import time

def weather_data():
    api_key = '850e318618e1ce4fba59799d09816304'
    url = f'http://api.openweathermap.org/data/2.5/weather?q=dhaka&appid={api_key}'

    def get_weather():
        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                weather = data['weather'][0]['description']
                temperature = data['main']['temp']
                city = data['name']
                feels_like = data['main']['feels_like']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']

                print(f'City: {city}')
                print(f'Weather: {weather}')
                print(f'Temperature: {temperature} K')
                print(f'Feels: {feels_like} K')
                print(f'Humidity: {humidity}%')
                print(f'Wind Speed: {wind_speed} m/s')
            else:
                print(f'Error: {data["message"]}')
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')

    while True:
        get_weather()
        print('Waiting for the next update...')
        time.sleep(1800)

weather_data()
