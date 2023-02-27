# Level 26 - Level 27: Bandit - OverTheWire

## Level Goal

Good job getting a shell! Now hurry and grab the password for bandit27!

## Solution
This level is a direct continuation of the previous level. While we are in the file editing state, we can run `:set shell=/bin/bash` to change the shell back to `/bin/bash`. We can then run `:shell` to spawn that shell.

From there, retrieving the password for `bandit27` is quite trivial. We can run the `./bandit27-do` file to `cat /etc/bandit_pass/bandit27` which will execute as `bandit27` (setuid) and reveal the password.

```bash
:set shell=/bin/bash
:shell
```

```bash
bandit26@bandit:~$ ls
bandit27-do  text.txt
bandit26@bandit:~$ ./bandit27-do 
Run a command as another user.
  Example: ./bandit27-do id
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS
```