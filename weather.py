import forecastio
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather(address):
	api_key = os.environ['WEATHER_API_KEY']
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	latitude = location.latitude
	longitude = location.longitude
	forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
	summary = forecast.temperature
	return "{} and {}° at {}".format(forecast.summary, forecast.temperature, location.address)

