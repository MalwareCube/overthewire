# Level 1 - Level 2: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in a file called `-` located in the home directory.

## Solution
First, connect to bandit1 using the password uncovered on Level 0-1. To obtain the flag for this level, we have to use `cat` to read a file that has a single dash (-) as the filename. This cannot be done through the expected means (ie: `cat -` as the `-` dash is used for specifying named arguments in a binary. For example, using `ssh -p`; the `-p` argument requires the use of the dash is used to specify the port to be used. In this case, we will have to specify the exact path of the file by combining the `./` (used to specify the current directory and the filename `-`:

```bash
bandit1@bandit:~$ cat ./-
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
```