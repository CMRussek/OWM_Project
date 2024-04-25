  
import logging.config
import os
from pathlib import Path
from WeatherAPI import WeatherAPI
from DataProcessor import DataProcessor
from DatabaseManager import DatabaseManager

os.chdir(Path(__file__).parent)
   
# Configure logging
logging.config.fileConfig('logging_config.ini')

city_name = input("Enter city name: ")
country_code = input("Enter country code: ")
api_key = "bf74a3d336b9f22dd6af67b521a73839"

logging.info(f"Starting weather script for city: {city_name}, country code: {country_code}")

weather_api = WeatherAPI(city_name, country_code, api_key)
city_id = weather_api.get_city_id()
weather_data = weather_api.get_weather_data()

if weather_data:
    logging.info("Successfully retrieved weather data")
    data_processor = DataProcessor(weather_data, city_id)
    processed_data = data_processor.process_data()

    if processed_data:
        temperature, max_temperature, min_temperature, description = processed_data
        database_manager = DatabaseManager(city_id, temperature, max_temperature, min_temperature, description)
        database_manager.save_to_database()
        logging.info("Data saved to database successfully!")
        
    else:
        logging.error("Failed to process weather data")
        
else:
    logging.error("Failed to fetch weather data")
    




   

    

    
