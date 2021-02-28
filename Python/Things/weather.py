from pyowm import OWM

owm = OWM('OWM_API')  # You MUST provide a valid API key

city= input('Введите город/страну: ')

# Search for current weather in London (Great Britain)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
print(w,"\n")                  # <Weather - reference time=2013-12-18 09:20, status=Clouds>

# Weather details
print("wind:",w.wind()["speed"],"m/s","\n")   # {'speed': 4.6, 'deg': 330}
print("humidity:",w.humidity,"%","\n")  # 87
print("temperature:", w.temperature('celsius')["temp"],"celsius","\n")  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
input("End",)
