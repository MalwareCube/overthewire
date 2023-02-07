# Level 31 - Level 32: Bandit - OverTheWire

## Level Goal

There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo. The password for the user bandit31-git is the same as for the user bandit31.

Clone the repository and find the password for the next level.

## Solution

```bash
bandit31@bandit:~$ mktemp -d
/tmp/tmp.q0XtUDLkF7
bandit31@bandit:~$ cd /tmp/tmp.q0XtUDLkF7
bandit31@bandit:/tmp/tmp.q0XtUDLkF7$ git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
Cloning into 'repo'...
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), 381 bytes | 381.00 KiB/s, done.

bandit31@bandit:/tmp/tmp.q0XtUDLkF7$ cd repo
bandit31@bandit:/tmp/tmp.q0XtUDLkF7/repo$ ls
README.md
bandit31@bandit:/tmp/tmp.q0XtUDLkF7/repo$ cat README.md 
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

bandit31@bandit:/tmp/tmp.q0XtUDLkF7/repo$ echo "May I come in?" > key.txt
bandit31@bandit:/tmp/tmp.q0XtUDLkF7/repo$ ls
key.txt  README.md
bandit31@bandit:/tmp/tmp.q0XtUDLkF7/repo$ git add key.txt
The following paths are ignored by one of your .gitignore files:
key.txt
hint: Use -f if you really want to add them.
hint: Turn this message off by running
hint: "git config advice.addIgnoredFile false"
bandit31@bandit:/tmp/tmp.q0XtUDLkF7/repo$ git add key.txt -f
bandit31@bandit:/tmp/tmp.q0XtUDLkF7/repo$ git commit -m "uploaded key.txt"
[master e4868df] uploaded key.txt
 1 file changed, 1 insertion(+)
 create mode 100644 key.txt
bandit31@bandit:/tmp/tmp.q0XtUDLkF7/repo$ git push origin master
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.

bandit31-git@localhost's password: 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 328 bytes | 328.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: ### Attempting to validate files... ####
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
remote: Well done! Here is the password for the next level:
remote: rmCBvG56y58BXzv98yZGdO7ATVL5dW8y 
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
To ssh://localhost:2220/home/bandit31-git/repo
```