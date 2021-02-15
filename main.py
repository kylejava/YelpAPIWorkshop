import requests
import json
from pprint import pprint


city = (input("What is your city? "))
food =(input("What would you like to search for? "))

API_key = 'Your API Key'
client_id = 'Your Client ID'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'Bearer %s' % API_key}
PARAMETERS = {
    'term': food,
    'limit': 10,
    'radius': 10000,
    'location': city,
    'offset':1

}

response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
data = response.json()

for place in data['businesses']:
    print(place['name'])
