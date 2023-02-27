# Level 18- Level 19: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in a file readme in the home directory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

## Solution
When using SSH to connect to `bandit18`, we are immediately logged out because the `.bashrc` file has been modified. To get around this and read the `readme` file, we can simply append the command `cat ~/readme` to cat the file `readme` from the user's home directory upon login. This will allow us to retrieve the output (the next level's password) before we are immediately logged out.

```bash
$ ssh bandit18@bandit.labs.overthewire.org -p 2220 'cat ~/readme'
bandit18@bandit.labs.overthewire.org's password: 
awhqfNnAbc1naukrpqDYcF95h7HoMTrC
```