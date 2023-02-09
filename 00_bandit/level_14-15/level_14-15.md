# Level 14 - Level 15: Bandit - OverTheWire

## Level Goal

The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

## Solution
For this level, we get to use `nc` - netcat. To put it simply, the Netcat ( nc ) command is a command-line utility for reading and writing data between two computer networks, and is also known as the "TCP/IP swiss army knife" due to how many uses it has.

The goal to retrieve the password is to submit the password of the current level to port 30000 on localhost. We can set this up using the following syntax: `nc localhost 30000`

The above syntax will set up a nc connection on "localhost" (127.0.0.1) and we then specify the port 30000. Once the connection has been set up, we can write data between the network - we can paste the level's current password which will then retrieve the password for the next level. 


```bash
bandit14@bandit:~$ nc localhost 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

bandit14@bandit:~$ nc 127.0.0.1 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

```