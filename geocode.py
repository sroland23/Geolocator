import requests
import json
from pprint import pprint
import pandas as pd

address = '1600 Amphitheatre Parkway, Mountain View, CA'
apikey = 'AIzaSyC7cdBVTqxjJDD0jkUtlObYRveKePy38GY'

response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address.replace('','+'), apikey))

resp_json_payload = response.json()['results'][0]
lat = resp_json_payload['geometry']['location']['lat']
lng = resp_json_payload['geometry']['location']['lng']

for item in resp_json_payload['address_components']:
    for category in item['types']:
        resp_json_payload[category] = item['short_name']
    final_state = resp_json_payload.get("administrative_area_level_1", None)
print('Latitude: ', lat)
print('Longitude: ',lng)
print('State: ',    final_state)
