# Level 12 - Level 13: Bandit - OverTheWire

## Level Goal

The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: `mkdir /tmp/myname123`. Then copy the datafile using cp, and rename it using mv (read the manpages!)

## Solution



```bash
bandit12@bandit:~$ ls -a
.  ..  .bash_logout  .bashrc  data.txt  .profile
bandit12@bandit:~$ mkdir /tmp/elliot
bandit12@bandit:~$ cp data.txt /tmp/elliot
bandit12@bandit:~$ cd /tmp/elliot
bandit12@bandit:/tmp/elliot$ mv data.txt hexdump.txt
bandit12@bandit:/tmp/elliot$ xxd -r hexdump.txt > compbinary
bandit12@bandit:/tmp/elliot$ file compbinary
compbinary.gz: gzip compressed data, was "data2.bin", last modified: Wed Jan 11 19:18:38 2023, max compression, from Unix, original size modulo 2^32 572
bandit12@bandit:/tmp/elliot$ mv compbinary compbinary.gz
bandit12@bandit:/tmp/elliot$ gzip -d compbinary
bandit12@bandit:/tmp/elliot$ file compbinary 
compbinary: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/elliot$ mv compbinary compbinary.bz2
bandit12@bandit:/tmp/elliot$ bzip2 -d compbinary.bz2 
bandit12@bandit:/tmp/elliot$ file compbinary
compbinary: gzip compressed data, was "data4.bin", last modified: Wed Jan 11 19:18:38 2023, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/elliot$ mv compbinary compbinary.gz
bandit12@bandit:/tmp/elliot$ gzip -d compbinary.gz 
bandit12@bandit:/tmp/elliot$ file compbinary 
compbinary: POSIX tar archive (GNU)
bandit12@bandit:/tmp/elliot$ cp compbinary safe
bandit12@bandit:/tmp/elliot$ mv compbinary compbinary.tar
bandit12@bandit:/tmp/elliot$ tar xvf compbinary.tar 
data5.bin
bandit12@bandit:/tmp/elliot$ file data5.bin 
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/elliot$ mv data5.bin data6.tar
bandit12@bandit:/tmp/elliot$ tar xvf data6.tar 
data6.bin
bandit12@bandit:/tmp/elliot$ file data6.bin 
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/elliot$ mv data6.bin data7.bz2
bandit12@bandit:/tmp/elliot$ bzip2 -d data7.bz2 
bandit12@bandit:/tmp/elliot$ file data7
data7: POSIX tar archive (GNU)
bandit12@bandit:/tmp/elliot$ mv data7 data8.tar
bandit12@bandit:/tmp/elliot$ tar xvf data8.tar 
data8.bin
bandit12@bandit:/tmp/elliot$ file data8.bin 
data8.bin: gzip compressed data, was "data9.bin", last modified: Wed Jan 11 19:18:38 2023, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/elliot$ mv data8.bin data9.gz
bandit12@bandit:/tmp/elliot$ gzip -d data9.gz 
bandit12@bandit:/tmp/elliot$ file data9
data9: ASCII text
bandit12@bandit:/tmp/elliot$ cat data9
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

```