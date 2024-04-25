import sqlite3
import requests


class WeatherAPI:
    def __init__(self, city_name, country_code, api_key, units='metric', lang='en'):
        self.city_name = city_name
        self.country_code = country_code
        self.api_key = api_key
        self.units = units
        self.lang = lang
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_city_id(self):
        conn = sqlite3.connect('weather_data.db')
        c = conn.cursor()
        c.execute("SELECT city_id FROM cities WHERE city_name=? ", (self.city_name,))
        result = c.fetchone()
        conn.close()
        if result:
            return result[0]
        else:
            return None
        
    def get_weather_data(self):
        url = f"{self.base_url}?q={self.city_name},{self.country_code}&appid={self.api_key}&units={self.units}&lang={self.lang}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None