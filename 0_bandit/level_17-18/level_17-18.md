# Level 17- Level 18: Bandit - OverTheWire

## Level Goal

There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19

## Solution
- Log in using identify file RSA key from previous level.
- hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg

```bash
bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$ diff passwords.new passwords.old
42c42
< hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
---
> 810zq8IK64u5A9Lb2ibdTGBtlcSZsoe8

```