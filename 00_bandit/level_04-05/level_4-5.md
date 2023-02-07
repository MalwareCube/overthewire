# Level 4 - Level 5: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in the only human-readable file in the `inhere` directory. Tip: if your terminal is messed up, try the “reset” command.

## Solution
The solution for this level requires us to use a number of tricks we've already used in previous levels. First off, `cd` into the `inhere` directory and run `ls -a` to list all the files (and ensure we're not missing anything hidden). We can see each file begins with a `-` character, which we will have to use the absolute path `./-` trick (from Level 1-2) when entering any of these files as a command argument. The description for this level mentions the password is stored in the only human-readable file. An easy way to detect this sort of thing is to run the `file` command against each file in the directory. The `file` command simply determines a file's type and displays it in the standard output.

We can use an asterisk `*` as a wildcard character when running the `file` command with a file name as an argument. This will allow us to run the `file` command against every file in the directory at once. By running `file ./-file0*` it will determine the file type for each file, and we can easily see that `-file07` is the only file listed as ASCII text. Because the remaining files were classified as the undetermined `data` type, it's safe to say `-file07` is likely the correct file that contains human-readable (ASCII) text. By using `cat` on that file, we can obtain the password for this level:

```bash
bandit4@bandit:~/inhere$ ls -a
.   -file00  -file02  -file04  -file06  -file08
..  -file01  -file03  -file05  -file07  -file09
bandit4@bandit:~/inhere$ file ./-file0*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
```