import requests 
from pprint import pprint
from config import open_weather_token

def getWeather(city, open_weather_token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={open_weather_token}&units=metric",
        )
        data = r.json()
        # pprint(data)


        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']

        print(f'температура {cur_weather} влажность {humidity} давление {pressure} ')
    except Exception as ex:
        print(ex)
        print('проверь название города ')

def main():
    city = input('город: ')
    getWeather(city, open_weather_token )


if __name__ == '__main__':
    main()