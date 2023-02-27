import requests
import re

username = 'natas0'
password = 'natas0'

url = f"http://{username}.natas.labs.overthewire.org/"

response = requests.get(url, auth = (username, password) )

print(re.findall('natas1 is (.*) -->', response.text)[0])
