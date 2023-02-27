# Level 32 - Level 33: Bandit - OverTheWire

## Level Goal

After all this git stuff its time for another escape. Good luck!

## Solution
For this level, we find ourselves in a strange shell which translates everything to UPPERCASE. This makes it next to impossible to run any commands, as `ls` gets translated to `LS`, which is not a valid binary.

To get around this, we need to think about what's going on here. If we pass the first argument variable `$0`, this will essentially pass the script to itself, breaking us out of the uppercase script. Once running this, we'll be in a normal bash shell, and if we run `ls`, we can see the `uppershell` binary that was translating everything to uppercase.

From here, we can now `cat /etc/bandit_pass/bandit33` to obtain the password for the next level.

```bash
WELCOME TO THE UPPERCASE SHELL
>> ls
sh: 1: LS: not found
>> $0
$ ls
uppershell
$ cat /etc/bandit_pass/bandit33
odHo63fHiFqcWWJG9rLiLDtPm45KzUKy

```