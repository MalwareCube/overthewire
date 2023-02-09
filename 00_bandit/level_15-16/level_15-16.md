# Level 15 - Level 16: Bandit - OverTheWire

## Level Goal

The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…

## Solution
For this level, we can use the `openssl` utility to establish a secure SSL connection to localhost on port 30001. The `s_client` command implements a generic SSL/TLS client which connects to the remote host using SSL/TLS. 

The `-connect` flag is used to make the connection, we specify the target `localhost:30001` and finally, the `-ign_eof` flag is used to inhibit shutting down the connection when end of file is reached in the input. Essentially, `-ign_eof` (ignore end of file) allows us to actually receive the password without the connection immediately shutting down. 

Putting that all together, we can create the connection, paste the current level's password, and receive the password for the next level.

```bash
bandit15@bandit:~$ openssl s_client -connect localhost:30001 -ign_eof
...
...
...
---
read R BLOCK
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1

closed
```