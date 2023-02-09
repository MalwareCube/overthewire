# Level 13 - Level 14: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on.

## Solution
For this level, when connecting to the server, we find the `sshkey.private` file, which is a private SSH key. We can simply `cat` out the file, and copy its contents on our local machine for later use. Now, we can SSH into the next level (bandit14) using bandit14's identity file (`sshkey.private`). You may need to use `chmod 600` on the key file to ensure has the correct permissions (only read/writable by the owner) to be used as an SSH key file. 

Once connected, the password can be found under `/etc/bandit_pass/bandit14` - since we are now `bandit14`, we have permissions to read the file.


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