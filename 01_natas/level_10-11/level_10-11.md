# Level 10 - Level 11: Natas - OverTheWire

## Level Goal

Username: natas11
URL:      http://natas11.natas.labs.overthewire.org

## Solution
This level really steps it up and uses an [exclusive or](https://en.wikipedia.org/wiki/XOR_cipher#cite_note-2) (`XOR`) encrypted cookie. Firstly, by viewing the sourcecode, we can see the client-side code and PHP which handles the setting, retrieving, encoding, and evaluation of a cookie.

We can see that a defualt array is created with a "showpassword" property set to "no" and a "bgcolor" property set to "#ffffff" (white). 

```php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
```

The later seemingly controls the background color of the webpage, and the showpassword property appears to be evaluated later on in the code to reveal the password for the next level:

```php
if($data["showpassword"] == "yes") {
    print "The password for natas12 is <censored><br>";
}
```

Now our goal is clear, we must manipulate this array in some way after it has been initialized in order to trick the webserver into revealing the password.

By analyzing the rest of the script, we can see that three different functions are defined:
1. A function for carrying out a XOR encryption of data
2. A function for loading data (getting a cookie)
3. A function for saving data (setting a cookie)

By going back to the site and opening up the console from the developer's tools and typing: `document.cookie` you will see the stored cookie returned among other information the following:
`data=ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D`

Additionally, in line 21 of the sourcecode, a variable called `$tempdata` is initialized, which contains the value of `$_COOKIE["data"]` (the cookie stored in our browser and seen above). The cookie is decoded from base64, transformed by the `xor_encrypt` function, and then JSON decoded.

```php
$tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
```

What this essentially means, is that the default cookie that is set in our browser is actually an encoded string that represents meaningful data that is later evaluated by the webserver. Further down, we can see that the code validates the `$tempdata` value to ensure that the `bgcolor` and `showpassword` array values exist:

```php
if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
```

It is now clear that the seemingly random cookie actually represents an encoded version of the array previously initialized in the code. By putting this together, it is clear we must reverse engineer a cookie  that when decoded, contains the same array but with the showpassword property set to "yes".

After understanding XOR encryption more, we can infer that the encrypted text would be the cookie and the plain text would be the PHP array. We can use both of these pieces of text to obtain a valid key. With XOR encryption, we require 2 out of 3 pieces of information to infer the third (the key, the plaintext, or the ciphertext).

## Decrypting The Default Array

We can create our own PHP code to make this happen. First, let's create `deserialize.php`:

```php
<?php

$cookie=base64_decode('MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D');
$jsoncookie=json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));

function xor_encrypt($in, $json) {
    $key = $json;
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

print xor_encrypt($cookie, $jsoncookie);
?>
```
Using the original code from the sourcecode and changing it a bit, several things are being done:

1. It decodes a base64-encoded string (the default cookie that was set) into a variable called $cookie. The decoded value is `0l;$49-8?=!)9jvi 'ngk% '(#$3lrnh(.--(.n6)`. This will be used as our ciphertext (`$in`).

2. It creates a JSON object and encodes it into a string variable called `$jsoncookie`. The JSON object has two key-value pairs: "showpassword" with a value of "no", and "bgcolor" with a value of "#ffffff". This is reversing the `json_decode` function to encode the default array into JSON format. This is the plaintext version of the cookie, and what will be used as the `$out` variable.

3. It defines a function called `xor_encrypt` that takes in two parameters: `$in` (the input string to be encrypted) and `$json` (the key to use for encryption). The function uses XOR encryption to encrypt the input string using the key.

4. The last line executes the `xor_encrypt` function, and passes the ciphertext `$cookie` value and the plaintext `$jsoncookie` value. When executed, we will obtain the missing piece: the key!

```bash
└─$ php deserialize.php 
KNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKL     
```

We can see the repeating pattern `KNHL`, which is in fact the key. Because the key is smaller than the plaintext, it is repeated until the length matches the plaintext. This is a security risk as it makes it much easier to brute-force a smaller key length.

## Encrypting A Malicious COokie
Now that we know the key used for XOR encryption, we can modify the original array, change the showpassword value to `yes`, then encrypt it in the same way in order to generate a new cookie.

First, let's create `serialize.php`:

```php
<?php

$data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = 'KNHL';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

print base64_encode(xor_encrypt(json_encode($data)));

?>
```
This is a lightly modified version of the original website sourcecode. A description of what this code does:

1. It defines an array called `$data` with two key-value pairs: "showpassword" with a value of "yes", and "bgcolor" with a value of "#ffffff". This is our malicious plaintext that we can now encrypt to get a valid cookie.

2. It defines a function called `xor_encrypt` that takes in one parameter: `$in` (the input string to be encrypted). The function uses XOR encryption to encrypt the input string using the repeating key `KNHL`.

3. It uses the `json_encode` built in function to convert the $data array to a JSON object and passes the resulting string to the xor_encrypt function.

4. It uses the `base64_encode` function to encode the output of the `xor_encrypt` function and prints the resulting string.

In order, our payload goes from an altered php array, to a JSON encoded version of that array, encoded with XOR, encoded to base64.

By executing this code, we receive the following output, which is a valid cookie we can use to manipulate the webserver's logic:
`MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz`

Now all we have to do is edit the cookie in our browser, or just make a `curl` request to the webpage and injecting that string in the `data` cookie:

```bash
└─$ curl 'http://natas11.natas.labs.overthewire.org/' -s -u natas11:1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg \
     -H 'Cookie: data=MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz' | grep password
The password for natas12 is YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG<br>
```

And we've finally tricked the webserver and received the password.