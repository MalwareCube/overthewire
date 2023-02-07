# Level 20 - Level 21: Bandit - OverTheWire

## Level Goal

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think.

## Solution


```bash
bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ ./suconnect 
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.

bandit20@bandit:~$ nc -l 4444
^Z
[1]+  Stopped                 nc -l 4444
bandit20@bandit:~$ ./suconnect 4444
^Z
[2]+  Stopped                 ./suconnect 4444
bandit20@bandit:~$ fg 1
nc -l 4444
VxCazJaVykI6W36BkBU0mJTCM8rR95XT
^Z
[1]+  Stopped                 nc -l 4444
bandit20@bandit:~$ fg 2
./suconnect 4444
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Password matches, sending next password
bandit20@bandit:~$ fg 1
nc -l 4444
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq

```