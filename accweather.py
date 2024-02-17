import json
import time
import urllib.request

apiKey = "myBlHBXiQOCGOVYTKS0p2VdGnkItEwCE"
country_code = "ir"
city = input("enter city name: ")

key = ""


def getLocation(country_code, city):
    search_address = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey="+apiKey+"&q="+city
    with urllib.request.urlopen(search_address) as sa:
        data = json.loads(sa.read().decode())
    location_key = data[0]['Key']
    return location_key


key = getLocation(country_code, city)


def getForecast(location_key):
    daily_forcast_url = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" + \
        location_key+"?apikey="+apiKey+"&metric=true"
    with urllib.request.urlopen(daily_forcast_url) as dfu:
        data = json.loads(dfu.read().decode())
    for key1 in data["DailyForecasts"]:
        print("weather forcast for: "+key1["Date"])
        print("Min Temp in C is: " +
              str(key1["Temperature"]["Minimum"]["Value"]))
        print("Max Temp in C is: " +
              str(key1["Temperature"]["Maximum"]["Value"]))
        print("Day Forecast"+key1["Day"]["IconPhrase"])
        print("+++++++++++++++++++++++++++++++++++++++++")


def get_current_condition(location_key):
    current_condition_url = "http://dataservice.accuweather.com/currentconditions/v1/" + \
        location_key+"?apikey="+apiKey+"&details=true"
    with urllib.request.urlopen(current_condition_url) as ccu:
        data = json.loads(ccu.read().decode())
        print(data)
    print("Weather Condition is: {}".format(data[0]['WeatherText']))
    print("Da")


getForecast(key)
get_current_condition(key)
