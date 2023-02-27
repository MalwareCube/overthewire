# Level 4 - Level 5: Natas - OverTheWire

## Level Goal

Username: natas5
URL:      http://natas5.natas.labs.overthewire.org

## Solution
After running `./natas.sh` we can see the following message:

```html
<div id="content">
Access disallowed. You are not logged in</div>
````

It seems the webpage doesn't have anything else of interest, however, if we think about what "logging in" typically entails, there is usually a session or user `cookie` that is set in the browser.

If we re-run the `curl` command manually and include the `-v` flag, we will also get the HTTP response headers in the output. One of the headers we receive from the webserver is `Set-Cookie` which is the method used in HTTP requests to set a cookie in a users' browser.

```bash
< Set-Cookie: loggedin=0
```

It appears the server has set a cookie with the value of `0`, typically meaning `false` (where `1` = `true`). The solution of this level is likely to change this cookie to `1` to trick the webserver into thinking we're logged in. Future web requets made to the webserver will include this cookie with the value we set it to.

As has been the case with previous levels, there are several ways we can do this. I'll cover with `curl`, with a python script, and from within the browser itself.

## Bash one-liner
```bash
└─$ curl -s --request GET --cookie "loggedin=1" http://natas5.natas.labs.overthewire.org -u natas5:Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD | grep password
Access granted. The password for natas6 is fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR</div>
```

I have covered most of these `curl` flags before, but quickly:

* `-s`: Silent output (avoids progress bar in the output)
* `-u`: User credentials for HTTP basic authentication
* `--request`: Used to specify the request method we are making to the webserver
* `--cookie`: This is where we specify the cookies we want to inject into our request. In this case, we're setting `loggedin` to = `1` (as by default it is set to `0`, or "not logged in")

Then, we simply just `grep` for `password` to clean up the output.

## Python
```python
import requests

cookies = {
    'loggedin': '1',
}

response = requests.get(
    'http://natas5.natas.labs.overthewire.org',
    cookies=cookies,
    auth=('natas5', 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'),
)

print(response.text)
```
This Python script uses the requests library to make an HTTP GET request to `http://natas5.natas.labs.overthewire.org`.

The `cookies` dictionary sets a cookie in the request with the key `loggedin` and the value `1`.

The `requests.get()` function is used to make the `GET` request. The url argument specifies the URL to make the request to, and the cookies argument is used to pass the cookie dictionary to the request. The `auth` argument is used to specify HTTP Basic Authentication credentials.

Finally, the response text is printed using `print(response.text)`. The response text represents the HTML content of the page that was returned by the server in response to the `GET` request.

## Browser
In the browser (Firefox for example), we can simply open the Developer Tools (usually `F12`). Go under `Storage` > `Cookies` and you should see the cookie value set `loggedin: 0`. Simply double-click (or right click > edit) and change the `0` to a `1`. Refresh the page to make a new request with the new saved cookie value, and you should receive the password.