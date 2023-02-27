import requests
import re

cookies = {
    'loggedin': '1',
}

response = requests.get(
    'http://natas5.natas.labs.overthewire.org',
    cookies=cookies,
    auth=('natas5', 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'),
)

#print(response.text)

print(re.findall('natas6 is (.*)</div>', response.text)[0])  