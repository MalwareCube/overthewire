# Level 10 - Level 11: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in the file data.txt, which contains base64 encoded data.

## Solution
The solution for this level simply requires the use of the `base64` command. The password in this case was encoded in base64, so we'll need to provide the `-d` flag to `decode` the base64 data.


```bash
bandit10@bandit:~$ cat data.txt | base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
```