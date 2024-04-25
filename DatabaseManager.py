import sqlite3

class DatabaseManager:
    def __init__(self, city_id, temperature, max_temperature, min_temperature, description):
        self.city_id = city_id
        self.temperature = temperature
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.description = description

    def save_to_database(self):
        conn = sqlite3.connect('weather_data.db')
        c = conn.cursor()
        c.execute("INSERT INTO weather_data (fk_city_id, temperature, max_temperature, min_temperature, description) VALUES (?, ?, ?, ?, ?)",
                  (self.city_id, self.temperature, self.max_temperature, self.min_temperature, self.description))
        conn.commit()
        conn.close()