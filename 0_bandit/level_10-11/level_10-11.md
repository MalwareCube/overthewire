# Level 10 - Level 11: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in the file data.txt, which contains base64 encoded data.

## Solution



```bash
bandit10@bandit:~$ cat data.txt | base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
```