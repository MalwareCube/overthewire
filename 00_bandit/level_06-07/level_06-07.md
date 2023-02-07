# Level 6 - Level 7: Bandit - OverTheWire

## Level Goal

The password for the next level is stored somewhere on the server and has all of the following properties:

    owned by user bandit7
    owned by group bandit6
    33 bytes in size


## Solution
This solution involves the use of the `find` command, along with several arguments to match the specifications outlined in the level description. The `find` command is used to simply search all files in a given directory hierarchy (recursively). The level goal notes that the password is stored "somewhere" on the server.

Firstly, we'll specify the `find` command with the `/` as the first argument. This is to set the command to search the entire filesystem (starting from /).

Next we'll include the `-user` argument and set it to `bandit7`. The `user` argument will only find files owned by that user's uname/user ID. We'll also include the `-group` argument and set it to `bandit6`. The `group` argument will only find files owned by that group's gname/group ID.

After that, the `-size 33c` argument is set. This is to specifically find files that are 33 bytes in size, based on the specifications provided. The lowercase `c` signifies that we're looking to match `bytes` (rather than `k` `M` or `G` for kilobytes, megabytes, or gigabytes, respectively).

The `2>/dev/null` is the null device that will essentially hide any errors (typically Permission Denied messages) found in the standard error output (2), and directing them to `/dev/null`, which is a special device that discards data written to it. This is just to clean up the output.

Putting this all together, we obtain the password:


```bash
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
```