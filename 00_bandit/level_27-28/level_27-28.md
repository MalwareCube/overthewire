# Level 27 - Level 28: Bandit - OverTheWire

## Level Goal

There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo. The password for the user bandit27-git is the same as for the user bandit27.

Clone the repository and find the password for the next level.

## Solution

```bash
bandit27@bandit:~$ mktemp -d
/tmp/tmp.ehe1gTZFQ2
bandit27@bandit:~$ cd /tmp/tmp.ehe1gTZFQ2
bandit27@bandit:/tmp/tmp.ehe1gTZFQ2$ git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

bandit27@bandit:/tmp/tmp.ehe1gTZFQ2$ cd repo/
bandit27@bandit:/tmp/tmp.ehe1gTZFQ2/repo$ ls
README
bandit27@bandit:/tmp/tmp.ehe1gTZFQ2/repo$ cat README 
The password to the next level is: AVanL161y9rsbcJIsFHuw35rjaOM19nR
```