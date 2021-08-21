# Weather API
import requests

def format_response(weather_json):
    # format json data of weather
    try:
        city_name       = weather_json['name']
        condition       = weather_json['weather'][0]['description']
        temparature     = weather_json['main']['temp']
        icon_name       = weather_json['weather'][0]['icon']
        weather_report    = 'City: %s \nCondition: %s \nTemperature (°F): %s' % (city_name, condition, temparature)
    except:
        weather_report = 'OOPS!, Failed to retrieving informations'
        icon_name = ''
    return (weather_report, icon_name)

def weather_information(city_name):
    # get weather information by calling openweathermap api
    weather_key = '88b65ab0e776a7794644df157ff3843b'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city_name, 'units': 'imperial'}
    response = requests.get(url, params)
    # print(response)
    weather_json = response.json()
    # print(weather_json)
    weather_report = format_response(weather_json)
    return weather_report

print(weather_information('bng')) 