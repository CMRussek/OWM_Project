



class DataProcessor:
    def __init__(self, weather_data, city_id):
        self.weather_data = weather_data
        self.city_id = city_id

    def process_data(self):
        if self.weather_data:
            temperature = self.weather_data["main"]["temp"]
            max_temperature = self.weather_data["main"]["temp_max"]
            min_temperature = self.weather_data["main"]["temp_min"]
            description = self.weather_data["weather"][0]["description"]
            return temperature, max_temperature, min_temperature, description
        else:
            return None