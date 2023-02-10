# Level 20 - Level 21: Bandit - OverTheWire

## Level Goal

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think.

## Solution
This level will require establishing concurrent `nc` listeners to send and receive data back and forth on the same port, as well as the `fg` command to switch between them. 

Firstly, we can set up an initial `nc` listener on port 4444 with `nc -l 4444`. We can back out of this connection by typing `^Z` (ctrl + c).

Next, the `./suconnect` binary in the home directory has the `setuid` binary set, and is owned by `bandit21`. We can use this binary to connect to port 4444 to establish a connection with `./suconnect 4444`. Again, we can back out of this connection by typing `^Z` (ctrl + c).

Now that a connection has been made we can return to our first `nc` listener by using the command `fg` and supplying the argument `1`. From here, we're back in our `nc` listener, and we can provide (paste) the password from the previous level. We can then back out of the connection again to return to our recipient.

We can use the `fg` command again and supply the argument `2` to return to our second connection. We can see that the password was correct, and that the password for the next level was sent back to our original listener. We can stop this listener `^Z`, and `fg 1` to return, where we receive the password for the next level.

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