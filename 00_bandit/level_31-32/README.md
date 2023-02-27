# Level 31 - Level 32: Bandit - OverTheWire

## Level Goal

There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo. The password for the user bandit31-git is the same as for the user bandit31.

Clone the repository and find the password for the next level.

## Solution
The last `git` level so far! Firstly, clone the repo into a `tmp` directory. The `README.md` file asks us to push a file to the remote repository in order to retrieve the password. It also gives us the details of what to include in the file named `key.txt`.

First, we can create `key.txt` by running `echo "May I come in?"` and sending the output (`>`) to `key.txt`.

From here, there are a couple of `git` specific steps we need to perform. First we need to run `add key.txt` to stage the `key.txt` file in the commit. It then gives us a warning that the file path we are trying to add is actually part of the `.gitignore` file (a file which indicates which paths/files you want to exclude from git). So to get around this,w e can add `-f` to the `git add` command to force this.

Next, we need to run `git commit -m "enter text here"`. the `commit` command is used to add a text description to record the changes to the repository.

Lastly, we can run `git push origin master` to push the commit to the `master` branch. We can then retrieve the password from the verbose success messaging in the command line from the push.

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