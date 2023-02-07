# Level 9 - Level 10: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

## Solution



```bash
bandit9@bandit:~$ strings data.txt | grep "==="
c========== the
h;========== password
========== isT
n.E========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
```