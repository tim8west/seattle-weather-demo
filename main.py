import requests

# Documentation metaweather:
# https://www.metaweather.com/api/


_URL = 'https://www.metaweather.com/api/location/'

# Get the woeid
location_id = str(
  requests.get(_URL + 'search/?query=seattle').json()[0]['woeid'])

# Weather and weather state
weather = requests.get(_URL + location_id +'/').json()
weather_state = weather['consolidated_weather'][0]['weather_state_name']
temp = str(
    weather['consolidated_weather'][0]['the_temp'])
# Log
<<<<<<< HEAD
print 'location id: %s' % location_id
print 'weather state: %s' % weather_state
=======
print('location id: %s' % location_id)
print('weather state: %s' % weather_state)
>>>>>>> cc530bf5cc7a6b46d626ff74db2bbd399f42c9cf
print 'temp: %s' % temp

def get_temp():
    return temp;

def get_location_id():
    return location_id;
# TODO(cnishina): Convert to functions and add testing.
# TODO(cnishina): Add option to write to file.
