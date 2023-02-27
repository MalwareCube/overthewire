# Level 5 - Level 6: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in a file somewhere under the `inhere` directory and has all of the following properties:

    human-readable
    1033 bytes in size
    not executable


## Solution
This solution involves the use of the `find` command, along with several arguments to match the specifications outlined in the level description. The `find` command is used to simply search all files in a given directory hierarchy (recursively). To begin, `cd` to the `inhere` directory. Running `ls -a` shows a large number of sub-directories. Firstly, we'll specify the `find` command with the `./` as the first argument. This is to set the command to use our current directory (as we are currently in the `inhere` directory.)

Next we'll include the `-type` argument and set it to `f`. The `-type f` argument tells the `find` command to return only files. If you don't use it, the find command will returns files, directories, and other things like named pipes and device files that match the name pattern you specify.

After that, the `-size 1033c` argument is set. This is to specifically find files that are 1033 bytes in size, based on the specifications provided. The lowercase `c` signifies that we're looking to match `bytes` (rather than `k` `M` or `G` for kilobytes, megabytes, or gigabytes, respectively).

The last requirement is that the file we're looking for is *not* executable. To filter out executable files, we can set `! -executable` as the last argument. Typically, including the `-executable` argument will only find files that *are* executable. The exclamation mark `!` is used to signify **not**, as we are looking for files that are **not** executable.

Putting this all together, we obtain the password:


```bash
bandit5@bandit:~$ cd inhere
bandit5@bandit:~/inhere$ ls -a
.            maybehere02  maybehere06  maybehere10  maybehere14  maybehere18
..           maybehere03  maybehere07  maybehere11  maybehere15  maybehere19
maybehere00  maybehere04  maybehere08  maybehere12  maybehere16
maybehere01  maybehere05  maybehere09  maybehere13  maybehere17
bandit5@bandit:~/inhere$ find ./ -type f -size 1033c ! -executable
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
```