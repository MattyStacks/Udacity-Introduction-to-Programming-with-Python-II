# TO DO:
# 1. Have display_weather print the weather report.
# 2. Handle network errors by printing a friendly message.
#
# To test your code, open a terminal below and run:
#   python3 weather.py


import requests
import os


API_ROOT = 'https://api.openweathermap.org/'
API_LOCATION = '/api/location/search/?query='
API_LOCATION25 = '/data/2.5/weather?q='
API_FORCAST = '/data/2.5/forecast?q='
API_WEATHER = '/api/location/'  # + woeid
API_KEY = '&appid=' + os.environ['API_KEY']

# try:
#     br = requests.get("https://googlis3432.com")
#     print(br.status_code)
# except requests.exceptions.ConnectionError:
#     print("Recieved a connection Error")

def fetch_location(query):
    return requests.get(API_ROOT + API_LOCATION25 + query + API_KEY).json()

    # print(API_ROOT + API_LOCATION25 + query + API_KEY)
    # return requests.get(API_ROOT + API_LOCATION25 + query + API_KEY).json()

def fetch_weather(city):
    print(API_ROOT + API_FORCAST + city + API_KEY)
    return requests.get(API_ROOT + API_FORCAST + city + API_KEY + '&units=imperial').json()

def display_weather(weather):
    print(f"Weather for {weather['city']['name']}:")
    for forecast_item in weather["list"]:
        print(f"The forcast for the date and time: {forecast_item['dt_txt']} The temp will be: {forecast_item['main']['temp']}")
    print("Replace this message with the weather report!")

def disambiguate_locations(locations):
    print("Ambiguous location! Did you mean:")
    for loc in locations:
        print(f"\t* {loc['title']}")

def weather_dialog():
    try:
        where = ''
        while not where:
            where = input("Where in the world are you? ")
        locations = fetch_location(where)
        # print(locations)
        if locations['cod'] == '404':
        # if len(locations) == 0:
            print("I don't know where that is.")
        # elif len(locations) > 1:
        #     disambiguate_locations(locations)
        else:
            city = locations['name']
            print(city)
            # print(fetch_weather(city))
            display_weather(fetch_weather(city))
    except requests.exceptions.ConnectionError:
        print("Check your network connection")

if __name__ == '__main__':
    while True:
        weather_dialog()