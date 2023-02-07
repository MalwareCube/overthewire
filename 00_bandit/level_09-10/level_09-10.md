# Level 9 - Level 10: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

## Solution
The solution for this level requires the use of the `strings` command to identify all printable / human-readable strings in the file. However, this will result in much more output than intended. To filter this further, we can send the output (using a | pipe) of the `strings data.txt` command to `grep`, where we can search for several `===` characters. This then prints out the human-readable lines that contain several "=" characters, giving us the intended output of the password.


```bash
bandit9@bandit:~$ strings data.txt | grep "==="
c========== the
h;========== password
========== isT
n.E========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
```