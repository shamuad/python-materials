import urllib2
import json

print "Welcome to mock weather"
country_input = raw_input("Enter country code : ")
city_input = raw_input("Enter city : ")


def get_weather_response():
    response = urllib2.urlopen("http://www.mocky.io/v2/57544c6a120000022d47761a").read()
    return json.loads(response)


def get_weather(country_code, city):
    get_all_weather_info = get_weather_response()
    all_counties = get_all_weather_info["Countries"]

    cities = []

    for country in all_counties :
        if country["CountryCode"] == country_code :
            cities = country["Cities"]

    requested_city = None
    for c in cities :
        if c["CityName"] == city :
            requested_city = c

    print requested_city


get_weather(country_input, city_input)
