import requests
from requests import exceptions
from pprint import pprint

try:
    resp = requests.get("http://nonexistent.com")
    print(resp.status_code)
except exceptions.ConnectionError:
    print("ConnectionError")
