# Level 29 - Level 30: Bandit - OverTheWire

## Level Goal

There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo. The password for the user bandit29-git is the same as for the user bandit29.

Clone the repository and find the password for the next level.

## Solution

```bash
bandit29@bandit:~$ mktemp -d
/tmp/tmp.1JHWriwaJC
bandit29@bandit:~$ cd /tmp/tmp.1JHWriwaJC
bandit29@bandit:/tmp/tmp.1JHWriwaJC$ git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
Cloning into 'repo'...

bandit29@bandit:/tmp/tmp.1JHWriwaJC$ cd repo
bandit29@bandit:/tmp/tmp.1JHWriwaJC/repo$ ls
README.md
bandit29@bandit:/tmp/tmp.1JHWriwaJC/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

bandit29@bandit:/tmp/tmp.1JHWriwaJC/repo$ git log
commit 8159c819f4d37d9491254035c9e74ffcb316652e (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Wed Jan 11 19:18:54 2023 +0000

    fix username

commit 23706c87f70872af9f04744569f7b6273647fb14
Author: Ben Dover <noone@overthewire.org>
Date:   Wed Jan 11 19:18:54 2023 +0000

    initial commit of README.md

bandit29@bandit:/tmp/tmp.1JHWriwaJC/repo$ git branch -r
  origin/HEAD -> origin/master
  origin/dev
  origin/master
  origin/sploits-dev
bandit29@bandit:/tmp/tmp.1JHWriwaJC/repo$ git checkout origin/dev 
Note: switching to 'origin/dev'.

bandit29@bandit:/tmp/tmp.1JHWriwaJC/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS
```