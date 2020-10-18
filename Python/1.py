import pprint
import requests
from dateutil.parser import parse

class YahooWeatherForecast:
	def get (self, city):
		url = f"https://weather-ydn-yql.media.yahoo.com/forecastrss?location={city},ca&format=json"
		data = requests.get(url).json()
		forecast_data = data["forecasts", 'current_observation', 'atmosphere', 'astronomy', 'condition']
		forecast = []
		for day in forecast_data:
			forecast.append({'date': day_data['date'], 'high_temp': day_data['high']})
		return forecast	


class CityInfo:
	def __init__ (self, city, weather_forecast = None):
		self.city = city
		self._weather_forecast = weather_forecast or YahooWeatherForecast()

	def weather_forecast (self):
		return self._weather_forecast.get(self.city)

def _main():
	city_info = CityInfo("Moscow",)
	forecast = city_info.weather_forecast()
	pprint.pprint(forecast)



if __name__ == "__main__":
	_main()