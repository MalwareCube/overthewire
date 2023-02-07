# Level 0: Bandit - OverTheWire

## Level Goal

The goal of this level is for you to log into the game using SSH. The host to which you need to connect is `bandit.labs.overthewire.org`, on `port 2220`. The username is `bandit0` and the password is `bandit0`. Once logged in, go to the Level 1 page to find out how to beat Level 1.

## Solution
To complete this level, we just need to make an SSH connection to bandit.labs.overthewire.org over port 2220. We've been given the correct credentials that we will be prompted for.

The syntax for making the SSH connection is the following:
`ssh bandit0@bandit.labs.overthewire.org -p 2220`

We then receive the following output, promting for the password (`bandit0`):

```bash
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit0@bandit.labs.overthewire.org's password:
```

Once we are authenticated, we can run a whoami to confirm that we are in fact the `bandit0` user:

```bash
bandit0@bandit:~$ whoami
bandit0
```

With that, Level 0 is now complete. We don't need to find any flags until Level 1.