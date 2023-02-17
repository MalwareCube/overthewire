# Level 10 - Level 11: Natas - OverTheWire

## Level Goal

Username: natas11
URL:      http://natas11.natas.labs.overthewire.org

## Solution

```bash
└─$ php deserialize.php
0l;$$98-8=?#9*jvi 'ngl*+(!$#9lrnh(.*-(.n67
{"showpassword":"no","bgcolor":"#ffffff"}
 Running xor_encrypt on cookie 
KNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKL
```

`KNHL`


```bash
└─$ curl 'http://natas11.natas.labs.overthewire.org/' -s -u natas11:1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg \
     -H 'Cookie: data=MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz' | grep password
The password for natas12 is YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG<br>
```