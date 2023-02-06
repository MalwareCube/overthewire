# Level 30 - Level 31: Bandit - OverTheWire

## Level Goal

There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo. The password for the user bandit30-git is the same as for the user bandit30.

Clone the repository and find the password for the next level.

## Solution

```bash
bandit30@bandit:~$ mktemp -d
/tmp/tmp.5PpolgSxSv
bandit30@bandit:~$ cd /tmp/tmp.5PpolgSxSv
bandit30@bandit:/tmp/tmp.5PpolgSxSv$ git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
Cloning into 'repo'...

bandit30-git@localhost's password: 
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
Receiving objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
bandit30@bandit:/tmp/tmp.5PpolgSxSv$ cd repo
bandit30@bandit:/tmp/tmp.5PpolgSxSv/repo$ ls
README.md
bandit30@bandit:/tmp/tmp.5PpolgSxSv/repo$ cat README.md 
just an epmty file... muahaha

bandit30@bandit:/tmp/tmp.5PpolgSxSv/repo$ git log
commit c027ef6d59c4031d56a6c6d16a526af0e8eb8383 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Wed Jan 11 19:18:56 2023 +0000

    initial commit of README.md

bandit30@bandit:/tmp/tmp.5PpolgSxSv/repo$ git branch -r
  origin/HEAD -> origin/master
  origin/master

bandit30@bandit:/tmp/tmp.5PpolgSxSv/repo$ git checkout origin/master
Note: switching to 'origin/master'.

bandit30@bandit:/tmp/tmp.5PpolgSxSv/repo$ git tag
secret
bandit30@bandit:/tmp/tmp.5PpolgSxSv/repo$ git show secret
OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt
```