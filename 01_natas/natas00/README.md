# Level 0: Natas - OverTheWire

## Level Goal

Username: natas0
Password: natas0
URL:      http://natas0.natas.labs.overthewire.org

## Solution
Unlike [bandit](https://github.com/odacavo/overthewire/tree/main/00_bandit), Natas is a web-based CTF. With that said, I would still like to implement scripting as much as I can throughout these challenges.

Each Natas challenge appears to use [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) to control the progression of each level, where we will need to submit the name of the current level (ex: `natas0`), as well as the password we retrieved from the previous level.

I've first created a simple `curl` script that will accept a username and password argument which should speed things up should we want to view a level in the commandline and work with it that way.

`natas.sh`:

```bash
#!/bin/bash

if [[ -z "$1" ]] || [[ -z "$2" ]]; then
        echo "Usage: ./natas.sh levelname password"
else
        curl http://$1.natas.labs.overthewire.org -u $1:$2
fi
```

You can see from the above script, it will take in argument `$1` as the username and `$2` as the password. It will then fill in these argument variables with the `curl -u` flag, to specify credentials for HTTP authentication.

The `if` statement is simply checking if `$1` and `$2` are empty, and if so, echoing out an error displaying the expected syntax.

Putting that all together, we are given the password for level 0, which is `natas0`. From within the level's directory, we can run `../natas.sh natas0 natas0`.

Based on the output, we can see the password is included in an HTML comment, which we could have also found by manually navigating to the site, and viewing the page source code. This way was quicker, and we can even filter this further by passing/piping the output (`|`) to `grep` and searching for `password`.

```bash
└─$ ../natas.sh natas0 natas0 | grep password
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   918  100   918    0     0   2852      0 --:--:-- --:--:-- --:--:--  2859
You can find the password for the next level on this page.
<!--The password for natas1 is g9D9cREhslqBKtcA2uocGHPfMZVzeFK6 -->
```