# Level 2 - Level 3: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in a file called `spaces in this filename` located in the home directory.

## Solution
First, connect to bandit2 using the password uncovered on Level 1-2. To obtain the flag for this level, we have to use `cat` to read a file that has explicit spaces within the filename. This cannot be done through the expected means (ie: `cat spaces in this filename` as each word (separated by a space) would be taken as a separate argument for the `cat` command. We would receive the four separate errors seen below, as none of these files exist in the current directory:

```bash
bandit2@bandit:~$ cat spaces in this filename
cat: spaces: No such file or directory
cat: in: No such file or directory
cat: this: No such file or directory
cat: filename: No such file or directory
```

In this case, we will have to enclose the filename within quotation marks so it is treated as a single argument:

```bash
bandit2@bandit:~$ cat "spaces in this filename"
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
```