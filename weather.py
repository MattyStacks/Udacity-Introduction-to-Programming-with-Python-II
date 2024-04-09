import requests
import json

# Had to modify the lesson to just use the example data that was provided. Below would be the call for the API
# r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Indianapolis&appid=***')
# print(r.json())


# Opening JSON file
f = open('weather_data.json')
data = json.load(f)

#Adding code to print date and humdity for all six days.
# date = data["consolidated_weather"][0]["applicable_date"]


print(data["consolidated_weather"][0]["applicable_date"])
print(data["consolidated_weather"][0]["humidity"])
print(data["consolidated_weather"][1]["applicable_date"])
print(data["consolidated_weather"][1]["humidity"])
print(data["consolidated_weather"][2]["applicable_date"])
print(data["consolidated_weather"][2]["humidity"])
print(data["consolidated_weather"][3]["applicable_date"])
print(data["consolidated_weather"][3]["humidity"])
print(data["consolidated_weather"][4]["applicable_date"])
print(data["consolidated_weather"][4]["humidity"])
print(data["consolidated_weather"][5]["applicable_date"])
print(data["consolidated_weather"][5]["humidity"])

for weather_date in data["consolidated_weather"]:
    print(weather_date["applicable_date"])
    print(weather_date["humidity"])
    print(f"The humdiity for {weather_date['applicable_date']} is {weather_date['humidity']}")
# Iterating through the json
# list
# for i in data['emp_details']:
#     print(i)
# print(data)
# Closing file
f.close()