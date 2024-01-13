import requests

response = requests.get('https://ipinfo.io/json')
location_info = response.json()

location = location_info['city']

weather_response = requests.get(f'https://wttr.in/{location}?0T')
print(weather_response.text)
