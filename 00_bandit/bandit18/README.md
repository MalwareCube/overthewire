# Level 17- Level 18: Bandit - OverTheWire

## Level Goal

There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19

## Solution
After using SSH with the previous level's identity (SSH key) file, we can connect to `bandit17`. For this level, we simply need to use the `diff` command, which will compare two files line by line and provide a verbose output on which lines have changed between the two. By running `diff`, we can put the new password file `passwords.new` as the first argument, and the old password file `passwords.old` as the second argument.

The output of this command will then show us the following line that was updated/changed in the new file `hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg`, which is the password for the next level. The `>` character indicates the addition or change in the new file.

```bash
bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$ diff passwords.new passwords.old
42c42
< hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
---
> 810zq8IK64u5A9Lb2ibdTGBtlcSZsoe8

```