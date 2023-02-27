import requests
import re

username = 'natas8'
password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'

url = f"http://{username}.natas.labs.overthewire.org/"

response = requests.post(url, data = {"secret": "oubWYf2kBq", "submit": "submit"}, auth = (username, password) )

#print(response.text)

print(re.findall('natas9 is (.*)', response.text)[0])
