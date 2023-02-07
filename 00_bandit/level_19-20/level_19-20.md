# Level 19 - Level 20: Bandit - OverTheWire

## Level Goal

To gain access to the next level, you should use the setuid binary in the home directory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

## Solution


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