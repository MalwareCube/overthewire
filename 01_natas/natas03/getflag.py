import requests
import re

username = 'natas3'
password = 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q'

url = f"http://{username}.natas.labs.overthewire.org/" + "s3cr3t/users.txt"

response = requests.get(url, auth = (username, password) )

#print(response.text)

print(re.findall('natas4:(.*)\n', response.text)[0])
