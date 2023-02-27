import requests
import re

username = 'natas1'
password = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'

url = f"http://{username}.natas.labs.overthewire.org/"

response = requests.get(url, auth = (username, password) )

#print(response.text)

print(re.findall('natas2 is (.*) -->', response.text)[0])
