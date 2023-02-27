# Level 21 - Level 22: Bandit - OverTheWire

## Level Goal

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

## Solution
This level requires taking advantage of a `cron` job that runs every minute. First, we can `cat` the cron job at `/etc/cron.d/cronjob_bandit22`. From the output, we can see that it runs every minute (`* * * * *`, look up [https://crontab.guru/](https://crontab.guru/) for more info on this). Additionally, the job executes `/usr/bin/cronjob_bandit22.sh` and sends any output to `/dev/null`. 

We can now `cat /usr/bin/cronjob_bandit22.sh` to see what is actually being executed every minute. From the output, we can see that the contents of `/etc/bandit_pass/bandit22` are being output (output copied with `>`) to `/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`. From here, it's just a matter of using `cat` to reveal the contents of `/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`, where we then receive the password.

```bash
bandit21@bandit:~$ cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh 
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff
```