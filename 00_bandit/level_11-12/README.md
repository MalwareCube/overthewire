# Level 11 - Level 12: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions.

## Solution
The goal for this level indicates the use of a rot13 cipher, as the password has been rotated by 13 positions. The `tr` command is a filter that converts characters from one set to another. The arguments we're passing relate to the characters we're selecting and converting to. 

The first set specified set is [A-Za-z], which is a shorthand way of typing [ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz] - or selecting all lowercase and uppercase letters. The second set defines the position of characters we would like to convert to. [N-ZA-Mn-za-m] is a shorthand way of typing [NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm] - or the entire alphabet shifted (rotated) 13 positions forward.

`tr` then reads each character from stdin, and if a character appears in the first set, it is replaces it with the character in the same position in the second set, essentially shifting the entire dataset by 13 positions, revealing the correct password.


```bash
bandit11@bandit:~$ ls -a
.  ..  .bash_logout  .bashrc  data.txt  .profile
bandit11@bandit:~$ cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
```