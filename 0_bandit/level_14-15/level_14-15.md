# Level 14 - Level 15: Bandit - OverTheWire

## Level Goal

The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

## Solution



```bash
bandit14@bandit:~$ nc localhost 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

bandit14@bandit:~$ nc 127.0.0.1 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

```