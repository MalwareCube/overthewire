# Level 7 - Level 8: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in the file data.txt next to the word millionth.

## Solution
For this level, we can use the `grep` command to search for the `millionth` string in `data.txt`. This will simply cat out the file but only show us the line where the word "millionth" is displayed, which consequently reveals the password.


```bash
bandit7@bandit:~$ cat data.txt | grep millionth
millionth   TESKZC0XvTetK0S9xNwm25STk5iWrBvP
```