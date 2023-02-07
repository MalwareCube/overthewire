# Level 0 - Level 1: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in a file called `readme` located in the `home` directory. Use this password to log into `bandit1` using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

## Solution
First, connect back to bandit0 using the credentials listed on Level 0. To obtain the flag for this first level, we can simply cat the contents of the `readme` file listed in the `/home/bandit0` directory:

```bash
bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```