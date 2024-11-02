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

# webbrowser.open("file://" + os.getcwd() + "/skillsoft.html")

with open("test_file.txt", "w") as f:
    f.write("Samplefile to upload")

url = "http://httpbin.org/post"
files = {"files": open("test_file.txt", "rb")}
values = {"upload_file": "test_file.txt", "OUT": "csv"}
r_post = requests.post(url=url, files=files, data=values)
print(r_post.status_code)
print(r_post.url)
