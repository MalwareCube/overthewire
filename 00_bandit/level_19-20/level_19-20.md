# Level 19 - Level 20: Bandit - OverTheWire

## Level Goal

To gain access to the next level, you should use the setuid binary in the home directory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

## Solution
For this level, we don't have the required permission to read the `/etc/bandit_pass/bandit20` file as user `bandit19`. We can take advantage of the `bandit20-do` binary, which has the `setuid` bit set `-rwsr-x---`, where the `s` indicates the `setuid` bit. Normally, on a unix-like operating system, the ownership of files and directories is based on the default `uid` (user-id) and `gid` (group-id) of the user who created them. 

When the `setuid` bit is used, the behavior described above it’s modified so that when an executable is launched, it does not run with the privileges of the user who launched it, but with that of the file owner instead. And we can see the `bandit20-do` file is owned by `bandit20`, so if we were to execute it, it should execute with the privileges of the `bandit20` user.

In this case, the `bandit20-do` file is written to simply execute any given command argument, so we can essentially execute any command with the privileges of `bandit20`, who has permission to read the `/etc/bandit_pass/bandit20` file. Simply supplying the `cat /etc/bandit_pass/bandit20` argument to the `./bandit20-do` command execution will allow us to read the password for the next level.


```bash
bandit19@bandit:~$ cat /etc/bandit_pass/bandit20
cat: /etc/bandit_pass/bandit20: Permission denied

bandit19@bandit:~$ ls -al
total 36
drwxr-xr-x  2 root     root      4096 Jan 11 19:18 .
drwxr-xr-x 70 root     root      4096 Jan 11 19:19 ..
-rwsr-x---  1 bandit20 bandit19 14876 Jan 11 19:18 bandit20-do
-rw-r--r--  1 root     root       220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root      3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root     root       807 Jan  6  2022 .profile

bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
VxCazJaVykI6W36BkBU0mJTCM8rR95XT
```