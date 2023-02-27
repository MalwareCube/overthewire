# Level 2 - Level 3: Natas - OverTheWire

## Level Goal

Username: natas3
URL:      http://natas3.natas.labs.overthewire.org

## Solution
Upon using our `natas.sh` script and `curl`-ing the webpage, we can see that there is nothing of interest on the index page. However, there is a peculiar HTML comment:

```html
<!-- No more information leaks!! Not even Google will find it this time... -->
```

Google, and other search engines use web "robots" (crawlers or spiders) to scan and index websites for the purpose of generating search results. The robots visit each page on a website, follow the links on that page to other pages, and then continue the process until they have visited every page on the site.

The data that the robots collect is then used by the search engine to generate search results based on the relevance of the page content to a user's search query.

`robots.txt` is a file that webmasters create to instruct web crawlers which pages or sections of their website they want to disallow robots from accessing. This file is placed in the root directory of a website and specifies which pages or sections of the website should not be crawled by web robots.

This hint is enough to prompt us to check if there is a `/robots.txt` file on this webpage. Upon navigating to `http://natas3.natas.labs.overthewire.org/robots.txt`, we can see the following entry:

```txt
User-agent: *
Disallow: /s3cr3t/
```

It appears there is a `/s3cr3t/` directory on this webpage - and upon navigating to it, we see another index page containing a `users.txt` file. This file provides us with the password for `natas4`.

```txt
natas4:tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm
```

## Bonus

We can directly extract the password to a file using the following one-liner:

```bash
└─$ curl http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt -s -u natas3:G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q | cut -f 2 -d : > natas4.pass

└─$ cat natas4.pass 
tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm
```

A brief explanation for each flag:

* `curl -s`: Silent or quiet mode. Don't show progress meter or error messages
* `curl -u`: Specify the user name and password to use for server authentication
* `cut`: Remove sections from each line of files (we're using this to only extract the password, not the username)
* `cut -d`: specifies which character we are using as a delimiter to "cut" the string up
* `cut -f`: select only these fields (cut uses a delimiter to "cut" a string into multiple fields. Because our delimiter will slice the string at the `:` colon, the first field will contain `natas4` and the second field will contain just the password)