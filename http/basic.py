import requests
import json
from pprint import pprint

data = requests.get("http://swapi.dev/api/planets/3")

print(data)
print(data.headers)
# pprint(data.headers)
print(data.text)
json_data = json.loads(data.text)
print("json data   ::  ", json_data)
print(data.is_redirect)


data = requests.get("http://www.google.com")
print(data.headers["server"])
