# Level 3 - Level 4: Natas - OverTheWire

## Level Goal

Username: natas4
URL:      http://natas4.natas.labs.overthewire.org

## Solution
Running our `./natas.sh` script for this level produces the following message:

```txt
Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
```

My first instinct is that the server is looking for the `Referer` [HTTP request header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer). The `Referer` header allows a server to identify referring pages that people are visiting from or where requested resources are being used. This data is typically used for analytics, logging, optimized caching, etc. 

In this case, this header appears to be required and used for authentication. The server appears to require the `Referer` header to be set to `http://natas5.natas.labs.overthewire.org/`, and because we used `curl` to make the initial request, our `Referer` is empty.

There are many ways we can do this, but I'll first show it with `curl`, and then we can write a `python` script using the requests module to accomplish the same task.

## Bash one-liner

```bash
curl http://natas4.natas.labs.overthewire.org/ -s -u natas4:tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm \
-H "Referer: http://natas5.natas.labs.overthewire.org/" | grep password
```
Let's go over how this works.

First, we do a standard `curl` to the URL and include the credentials with the `-u` flag. Also, add `-s` to get an output without the progress bar.

Next, we add a `\` backslash to tell Bash that the following line continues the current line. This actually isn't needed (it can be all on one line, but this cleans up the input).

Next, we include the `-H` flag, which is used to inject headers within our `curl` command. The syntax for an HTTP header is `Header-Name: headervalue`. So we can simply inject the `Referer` header and give it the expected value of `http://natas5.natas.labs.overthewire.org/`.

Knowing what the output looks like, we can `| grep password` to quickly extract the password for `natas4`.

```bash
curl http://natas4.natas.labs.overthewire.org/ -s -u natas4:tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm \
-H "Referer: http://natas5.natas.labs.overthewire.org/" | grep password
```

## Python requests

```bash
└─$ vi natas3.py
```

```python
import requests

headers = {
    'Referer': 'http://natas5.natas.labs.overthewire.org/',
}

response = requests.get(
    'http://natas4.natas.labs.overthewire.org/',
    headers=headers,
    auth=('natas4', 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'),
)

print(response.text)
```

```bash
└─$ chmod +x natas3.py
└─$ python3 natas3.py
```

This python script uses the `requests` library in Python to make a `GET` request to the URL `http://natas4.natas.labs.overthewire.org`.

The request includes several parameters:

* headers: a dictionary that specifies the HTTP header for the request. In this case, it sets the `Referer` header to `http://natas5.natas.labs.overthewire.org/`.

* auth: a tuple that contains the username and password for HTTP basic authentication.

The `requests.get()` function sends the GET request and returns the response, which is stored in the response variable. The response can then be used to access the content, status code, headers, etc. of the server's response.

We finally use `print(response.text)` to "echo" the response text to the command line, revealing the password.

