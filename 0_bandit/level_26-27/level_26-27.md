# Level 26 - Level 27: Bandit - OverTheWire

## Level Goal

Good job getting a shell! Now hurry and grab the password for bandit27!

## Solution


```bash
:set shell=/bin/bash
:shell
```

```bash
bandit26@bandit:~$ ls
bandit27-do  text.txt
bandit26@bandit:~$ ./bandit27-do 
Run a command as another user.
  Example: ./bandit27-do id
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS
```