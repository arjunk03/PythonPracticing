import requests
import webbrowser
import os
from pprint import pprint

r_post = requests.post(
    "https://en.wikipedia.org/w/index.php", data={"search": "skillsoft"}
)
print(r_post.status_code)
print(r_post.text)

with open("skillsoft.html", "wb") as f:
    for chunk in r_post.iter_content(chunk_size=10000):
        f.write(chunk)

webbrowser.open("file://" + os.getcwd() + "/skillsoft.html")
