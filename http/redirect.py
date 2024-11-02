import requests
from pprint import pprint

resp = requests.get("http://gmail.com")
print(resp.history)
print(resp.status_code)
print(resp.url)
print(resp.history[0].url)
print(resp.history[1].url)
print(resp.history[2].url)
print(resp.is_redirect)
print(resp.history[0].is_redirect)
print(resp.history[1].is_redirect)
print(resp.history[2].is_redirect)
print(resp.history[2].is_permanent_redirect)
