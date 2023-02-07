# Level 8 - Level 9: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in the file data.txt and is the only line of text that occurs only once.

## Solution
To find the password in the `data.txt` file, we first want to sort each line lexicographically using the `sort` command. From there pipe `|` the output of that command into the `uniq` command. The `uniq` command is going to omit repeated lines, and because we've already ordered everything alphabetically, all of the repeated lines in the file will be removed. By adding the `-u` flag, this will ensure that only unique lines are printed to the output. Putting these commands together, we get the password:


```bash
bandit8@bandit:~$ sort data.txt | uniq -u
EN632PlfYiZbn3PhVK3XOGSlNInNE00t
```