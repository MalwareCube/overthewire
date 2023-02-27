# Level 22 - Level 23: Bandit - OverTheWire

## Level Goal

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

## Solution
The solution for this level requires parsing through another cronjob. Firstly, we can view the cronjob's configuration with `cat /etc/cron.d/cronjob_bandit23`. We can see that `/usr/bin/cronjob_bandit23.sh` is running every minute, and by viewing that executable, we can see that the script does a couple of things.

First, the script sets a variable for the output of the `whoami` command as `myname`. Since the user `bandit23` will run the script, we can infer any instance of that variable in the script will refer to `bandit23`. 

Second, the script echos the following string "I am `bandit23`" and pipes (`|`) the output to an md5 hash (`md5sum`), which is then piped to the `cut` command to remove any whitespace from the first delimiter field.

The script then copies the password file (from `/etc/bandit_pass/bandit23` to `/tmp/` + the output of the above hash).

To find the location of the tmp file, we can simply run the md5 line ourselves, putting bandit23 in place for the variable: `echo I am user bandit23 | md5sum | cut -d ' ' -f 1`. From the output, we get the hash which we can use to find the tmp directory where the password is created into.

```bash
bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh 
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget

bandit22@bandit:~$ echo I am user bandit23 | md5sum | cut -d ' ' -f 1
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G
```