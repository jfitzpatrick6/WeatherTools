## Name of file: EcmWeatherTools.py
## Description: functions to grab often used weather data points
## Last Edited: 9/19/2022
## Last Edited By: jfitzpatrick
## Time in Development: 1 hour

# GOALS

# 7 day forecast based on zipcode https://api.weather.gov/gridpoints/BOX/71,90
# avg hi/low this week
# avg humidity this week
# projected wind speeds/ direction
# solar radiation for solar power projections https://openweathermap.org/api/solar-radiation
# solar projections?
# wind projections

import requests
import pgeocode

def getforecast(latlong):
    url = 'https://api.weather.gov/points/' + str(latlong[0]) + ',' + str(latlong[1])

    r = requests.get(url)
    data = r.json()
    
    return data['properties']['forecast']

def weekforecast(zipcode):
    location = tolatlong(zipcode)

    URL = getforecast(location)

    r = requests.get(url = URL)
    data = r.json()['properties']['periods']
    print(data)

def solarRadiation(zipcode):
    return True

def windForecast(zipcode):
    return True

def humidityForecast(zipcode):
    return True

def tolatlong(zipcode):
    nomi = pgeocode.Nominatim('us')
    place = nomi.query_postal_code(zipcode)
    return [place['latitude'], place['longitude']]


weekforecast(14150)