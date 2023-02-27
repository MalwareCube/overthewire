# Level 0 - Level 1: Natas - OverTheWire

## Level Goal

Username: natas1
URL:      http://natas1.natas.labs.overthewire.org

## Solution
This level is a very easy solve as we've done the bulk of our work in `natas0` by writing the `natas.sh` script. The trick to this level is the same as the previous level, however the webpage has blocked the use of the right click with Javascript. 

It is still trivial to view the source code in a page that prevents right clicking (ex: `Ctrl + U` or appending `view-source:` to the beginning of the URL).

However, we can simply run `./natas.sh natas1 g9D9cREhslqBKtcA2uocGHPfMZVzeFK6 | grep password`.


```bash
└─$ ./natas.sh natas1 g9D9cREhslqBKtcA2uocGHPfMZVzeFK6 | grep password
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1063  100  1063    0     0   3379      0 --:--:-- --:--:-- --:--:--  3385
You can find the password for the
<!--The password for natas2 is h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7 -->
```
