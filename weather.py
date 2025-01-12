import requests
import os
import sys

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/3.0/onecall"

LATITUDE="40.8071"
LONGITUDE="-74.1960"

# Making the API request
def get_weather():
    url = f"{BASE_URL}?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}&units=metric" # Constructing the request URL
    response = requests.get(url)
    with open("output/output.txt", "a") as file:

    # Parsing the JSON response
        if response.status_code == 200:
            data = response.json()
            current = data['current']
            temp=current['temp']
            feels=current['feels_like']
            relative=current['humidity']
            dew=current['dew_point']
            uvi=current['uvi']
            clouds=current['clouds']
            visible=current['visibility']
            wind=current['wind_speed']
            #gust=current['wind_gust']
            weather = current['weather'][0]['main']
            description=current['weather'][0]['description']
            print(f"Latest Weather: {weather} --your location has {description}--", file=file)
            print(f"Temperature: {temp}°C", file=file)
            print(f"Feels Like: {feels}°C", file=file) 
            print(f"Relative Humidity: {relative}%", file=file)
            print(f"Dew Point: {dew}", file=file)
            #print(f"Weather: {weather}")
            #print(f"Details: {description}")
            print(f"UV Index: {uvi}", file=file)
            print(f"Clouds: {clouds}%", file=file)
            print(f"Visibility: {visible} Meters", file=file)
            print(f"Wind Speed: {wind} km/h", file=file)
            #print(f"Wind Gust: {gust} km/h")
            #print (current)
            hourly=data["hourly"]
            hourly_temp=hourly[0]['temp']
            hourly_feels=hourly[0]['feels_like']
            hourly_weather=hourly[0]['weather'][0]['main']
            hourly_description=hourly[0]['weather'][0]['description']
            hourly_relative=hourly[0]['humidity']
            hourly_dew=hourly[0]['dew_point']
            hourly_uvi=hourly[0]['uvi']
            hourly_clouds=hourly[0]['clouds']
            hourly_visible=hourly[0]['visibility']
            hourly_wind=hourly[0]['wind_speed']
            #hourly_gust=hourly[0]['wind_gust']
            print("-------------------------------------------", file=file)
            print ("In 1 Hour:", file=file)
            print (f"{hourly_weather} --expect {hourly_description}--", file=file)
            #print (f"Hourly Weather: {hourly_weather}")
            #print (f"Hourly Details: {hourly_description}")
            print (f"{hourly_temp}°C", file=file)
            print (f"Feels like: {hourly_feels}°C", file=file)
            print (f"Relative Humidity: {hourly_relative}%", file=file)
            print (f"Dew Point: {hourly_dew}", file=file)
            print (f"UV Index: {hourly_uvi}", file=file)
            print (f"Clouds: {hourly_clouds}%", file=file)
            print (f"Visibility: {hourly_visible} Meters", file=file)
            print (f"Wind Speed: {hourly_wind} km/h", file=file)
            #print (f"Wind Gust: {hourly_gust}")
            daily=data["daily"]
            daily_summary=daily[0]["summary"]
            daily_temp_day=daily[0]["temp"]["day"]
            daily_temp_night=daily[0]["temp"]["night"]
            daily_temp_max=daily[0]["temp"]["max"]
            daily_temp_min=daily[0]["temp"]["min"]
            daily_temp_eve=daily[0]["temp"]["eve"]
            daily_temp_morning=daily[0]["temp"]["morn"]
            daily_feels_day=daily[0]["feels_like"]["day"]
            daily_feels_night=daily[0]["feels_like"]["night"]
            daily_feels_eve=daily[0]["feels_like"]["eve"]
            daily_feels_morning=daily[0]["feels_like"]["morn"]
            daily_relative=daily[0]["humidity"]
            daily_dew=daily[0]["dew_point"]
            daily_clouds=daily[0]["clouds"]
            #daily_visible=daily[0]["visibility"]
            daily_wind=daily[0]["wind_speed"]
            print("-------------------------------------------", file=file)
            print (f"Tomorrow: {daily_summary} min {daily_temp_min}°C, max {daily_temp_max}°C", file=file)
            print (f"Day: {daily_temp_day}°C >>> Feels like {daily_feels_day}°C", file=file)
            #print (f"Feels like {daily_feels_day}")
            print (f"Night: {daily_temp_night}°C >>> Feels like {daily_feels_night}°C", file=file)
            #print (f"Feels like {daily_feels_night}")
            print (f"Morning: {daily_temp_morning}°C >>> Feels like {daily_feels_morning}°C", file=file)
            #print (f"Feels like {daily_feels_morning}")
            print (f"Evening: {daily_temp_eve}°C >>> Feels like {daily_feels_eve}°C", file=file)
            #print (f"Feels like {daily_feels_eve}")
            print (f"Relative Humidity: {daily_relative}", file=file)
            print (f"Dew Point: {daily_dew}", file=file)
            print (f"Clouds: {daily_clouds}%", file=file)
            print (f"Wind Speed: {daily_wind} km/h", file=file)
            
        else:
            print(f"Error: {response.status_code} - {response.text}", file=file)

get_weather()