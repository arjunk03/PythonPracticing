from re import search
import requests
import webbrowser

url = "https://www.wikipedia.org/"

resp_obj = requests.get(url)
print(resp_obj.url)

# webbrowser.open(resp_obj.url)

search_term = input("Enter the term you need to search :")

url = "https://www.youtube.com/search"
params = {"q": search_term}

r_get = requests.get(url=url, params=params)
print(r_get.url)

webbrowser.open(r_get.url)
