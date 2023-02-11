# Level 28 - Level 29: Bandit - OverTheWire

## Level Goal

There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo. The password for the user bandit28-git is the same as for the user bandit28.

Clone the repository and find the password for the next level.

## Solution
This level requires us to clone another `git` repo in a temporary directory. From here, we can see a `README.md` file, upon reading, shows potential credentials for the next level. However, the password has been replaced with `xxxxxxxxxx`. Because `git` is a version control system, we can potentially see if there are previous versions of this file, and if so, we can move back in time to try to reveal if the password was ever committed to the repo in cleartext.

To do this, run `git log`. From here, we can see two previous commits before the `HEAD` / current version. The current commit displays the comment `fix info leak` which means the password is likely in the previous commit. We can switch to that previous commit by running `git checkout 2c1f82f75ab09c89166dd9e6e351bf479fb2d48f` where that long hash relates to the commit itself.

Now that we've essentially gone "back in time", we can now `cat README.md` to reveal the cleartext password for the next level that was once committed into the repo.

```bash
bandit28@bandit:~$ mktemp -d
/tmp/tmp.9Ycg0tTTQ6
bandit28@bandit:~$ cd /tmp/tmp.9Ycg0tTTQ6
bandit28@bandit:/tmp/tmp.9Ycg0tTTQ6$ git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
Cloning into 'repo'...

Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
bandit28@bandit:/tmp/tmp.9Ycg0tTTQ6$ cd repo/
bandit28@bandit:/tmp/tmp.9Ycg0tTTQ6/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.9Ycg0tTTQ6/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx

bandit28@bandit:/tmp/tmp.9Ycg0tTTQ6/repo$ git log
commit c6dc61e6ffdc717253130886555d087cac472f50 (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Wed Jan 11 19:18:53 2023 +0000

    fix info leak

commit 2c1f82f75ab09c89166dd9e6e351bf479fb2d48f
Author: Morla Porla <morla@overthewire.org>
Date:   Wed Jan 11 19:18:53 2023 +0000

    add missing data

commit 444da53e268c462d39cf7441a3bbf7af1832e21f
Author: Ben Dover <noone@overthewire.org>
Date:   Wed Jan 11 19:18:53 2023 +0000

    initial commit of README.md


bandit28@bandit:/tmp/tmp.9Ycg0tTTQ6/repo$ git checkout 2c1f82f75ab09c89166dd9e6e351bf479fb2d48f
Note: switching to '2c1f82f75ab09c89166dd9e6e351bf479fb2d48f'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

bandit28@bandit:/tmp/tmp.9Ycg0tTTQ6/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.9Ycg0tTTQ6/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S

```