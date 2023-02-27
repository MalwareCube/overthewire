# Level 16 - Level 17: Bandit - OverTheWire

## Level Goal

The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

## Solution
First, we can conduct an `nmap` scan of the localhost (127.0.0.1) to discover which port has a server listening on it. We can specify the port range with the `-p` flag, and provide `31000-32000`. From there, the scan results in 5 potential options which we can attempt to connect to using the `openssl s_client -connect` command. Additionally, by adding the `ign_eof` flag per the previous level, we can ensure the connection won't immediately close.

By connecting to the correct listening port, we are able to submit the password for the current level to reveal the password for the next level. In this case, we get a private SSH key to use to SSH into the bandit17 user.


```bash
bandit16@bandit:~$ nmap 127.0.0.1 -p 31000-32000
Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-31 03:21 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000099s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.06 seconds

bandit16@bandit:~$ openssl s_client -connect localhost:31790 -ign_eof
...
...
---
read R BLOCK
JQttfApK4SeyHwDlI9SXGR50qclOAil1
Correct!
-----BEGIN RSA PRIVATE KEY-----
...
```