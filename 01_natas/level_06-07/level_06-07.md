# Level 6 - Level 7: Natas - OverTheWire

## Level Goal

Username: natas7
URL:      http://natas7.natas.labs.overthewire.org

## Solution

By using our `./natas.sh` `curl` script, we see the following output on the webpage:

```html
<a href="index.php?page=home">Home</a>
<a href="index.php?page=about">About</a>
<br>
<br>

<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
```

To me, this looks like the solution here is to exploit a directory traversal vulnerability. The comment in the HTML hints `/etc/natas_webpass/natas8` holds the password, and if we were able to print the contents of this file to the webpage, we'll be able to obtain the password.

The webpage also contains a navigation element, and the URLs in the anchor tags appear to pass in a filename (ex: `page=home`, `page=about`) as a query parameter in the URL. The webserver is likely using PHP to include these files.

Therefore, we can potentially exploit the URL parameter to include the `/etc/natas_webpass/natas8` file.

Typically, we can use multiple iterations of `../` to "walk" our way back into the filesystem, and eventually get to the root `/` directory. From there, we can add the intended path `etc/natas_webpass/natas8` and make the request to the webserver.

The full URL to test: `http://natas7.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8`

**Tip for future directory/path traversal attacks:** If you don't get the intended results or receive an error, you may need to back out of more directories (include more `../` iterations, depending on the filesystem structure).

Our final `curl` request will look like this:

```bash
└─$ curl "http://natas7.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8" -s -u natas7:jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr
```

And in the output, we receive the password:

```html
<br>
a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB
```

