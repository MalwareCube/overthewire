# Level 13 - Level 14: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on.

## Solution
- cat private key
- save to local file
- exit current ssh session, connect to `bandit14` using the identity key
- cat password


```bash
bandit13@bandit:~$ ls
sshkey.private
bandit13@bandit:~$ cat sshkey.private
```

```bash
`ssh bandit14@bandit.labs.overthewire.org -p 2220 -i key`
```

```bash
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
```