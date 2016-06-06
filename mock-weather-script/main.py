import urllib2
import json

print "Welcome to mock weather"
country_input = raw_input("Enter country code : ")
city_input = raw_input("Enter city : ")
unit_input = raw_input("Fahrenhit (F) / Celcius  (C) ? ")

def cel_to_fah(cel):
    fah = 9.0/5.0 * cel + 32
    return fah

def get_weather_response():
    response = urllib2.urlopen("http://www.mocky.io/v2/57553bec130000b2168ea365").read()
    return json.loads(response)

def get_weather(country_code, city, unit):
    get_all_weather_info = get_weather_response()
    all_counties = get_all_weather_info["Countries"]

    cities = []

    for country in all_counties:
        if country["CountryCode"] == country_code:
            cities = country["Cities"]

    requested_city = None
    for c in cities:
        if c["CityName"] == city:
            requested_city = c

    city_temp = requested_city["Temp"]["Value"]
    temp_unit = requested_city["Temp"]["Unit"]

    if unit == "F":
        city_temp = float(cel_to_fah(city_temp))
        temp_unit = "F"

    print city_temp, temp_unit

get_weather(country_input, city_input, unit_input)
