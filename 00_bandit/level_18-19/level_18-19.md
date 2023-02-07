# Level 18- Level 19: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in a file readme in the home directory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

## Solution


```bash
$ ssh bandit18@bandit.labs.overthewire.org -p 2220 'cat ~/readme'
bandit18@bandit.labs.overthewire.org's password: 
awhqfNnAbc1naukrpqDYcF95h7HoMTrC
```