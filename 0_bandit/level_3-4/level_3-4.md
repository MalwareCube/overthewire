# Level 3 - Level 4: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in a hidden file in the inhere directory.

## Solution
First, connect to bandit3 using the password uncovered on Level 2-3. The solution for this level requires the use of the `-a` argument for the `ls` command. The `-a` argument is used to list all files (including hidden ones). Hidden files are used all over the Linux filesystem are prefixed with a `.` within the filename. These hidden files will not typically show up when the `ls` command is used with no arguments.

To obtain the flag for this level, we have to use `cd` into the `inhere` directory. From there, we need to run `ls -a` to find all files in the directory. From there, we `cat` the `.hidden` file to reveal the password:

```bash
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ ls -a
.  ..  .hidden
bandit3@bandit:~/inhere$ cat .hidden
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
```