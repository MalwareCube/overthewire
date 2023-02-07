# Level 8 - Level 9: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in the file data.txt and is the only line of text that occurs only once.

## Solution



```bash
bandit8@bandit:~$ sort data.txt | uniq -u
EN632PlfYiZbn3PhVK3XOGSlNInNE00t
```