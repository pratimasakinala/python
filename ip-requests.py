import requests
import json

url = 'http://ipinfo.io/json'

response = requests.get(url)
data = response.json()

print('You are {ip} in {city}'.format(**data))
