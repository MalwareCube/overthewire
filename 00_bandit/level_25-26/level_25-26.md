# Level 25 - Level 26: Bandit - OverTheWire

## Level Goal

Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

## Solution
Upon logging into `bandit25`, we get an SSH key for user `bandit26`. We can then copy this locally and use it to SSH into `bandit26` with the key as the identity file. 

However, it seems that upon logging into `bandit26`, we are immediately logged out. This is because the shell for the user `bandit26` has been changed to something other than `/bin/bash`. We can verify this by returning to the `bandit25` user and running `cat /etc/passwd | grep bandit26`. The output will show us the `/etc/passwd` entry for `bandit26`, which shows that the shell has been replaced with `/usr/bin/showtext`, which is definitely not a shell.

We can `cat /usr/bin/showtext` to view what is actually going on. It simply reads a file in the user's home directory named `text.txt` using the `more` command (command line file viewer with pagination/one screen at a time).

The solution here is kind of hack-y. We need to get the `more` command to actually paginate the `text.txt` output, but since it's a small text file, we need to make our terminal window increasingly small in order to get this to execute.

From this state, we can press the `v` key, which is a function of `more` - this will put us in a text editor, where we can then run commands to read files within the system. By typing `:e /etc/bandit_pass/bandit26` we can actually read the contents of the file from within the text editor, from within `more`. Kind of crazy.

```bash
bandit25@bandit:~$ ls
bandit26.sshkey
bandit25@bandit:~$ cat bandit26.sshkey 
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEApis2AuoooEqeYWamtwX2k5z9uU1Afl2F8VyXQqbv/LTrIwdW
pTfaeRHXzr0Y0a5Oe3GB/+W2+PReif+bPZlzTY1XFwpk+DiHk1kmL0moEW8HJuT9
/5XbnpjSzn0eEAfFax2OcopjrzVqdBJQerkj0puv3UXY07AskgkyD5XepwGAlJOG
...
...
...

$ ssh -i key bandit26@bandit.labs.overthewire.org -p 2220
Connection to bandit.labs.overthewire.org closed.

bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext

bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

exec more ~/text.txt
exit 0
```

```bash
v
:e /etc/bandit_pass/bandit26
c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1
```