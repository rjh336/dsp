# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

* `pwd` - show current working directory path
* `mkdir` - creating a directory
* `rm -r` - deleting a directory
* `touch [filename]` - creating a file using `touch` command
* `rm [filename]` - deleting a file
* `mv [Path to filename] [Path to new filename]` - renaming a file
* `ls -la` - listing hidden files
* `cp [Path to file] [New Path]` - copying a file from one directory to another
* `grep [regex] *` - find all instances of a given regex in current directory
* `env` - list all environment variables
* `cat [filename]` - display contents of file in current directory to STDOUT
* `less [filename]` - view contents of file by page
* `sudo su` - switch user to root

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

`ls` - display contents of current directory  
`ls -a` - display all (including hidden) contents of current directory  
`ls -l` - display contents of current directory in long list format  
`ls -lh` - display file/folder sizes of current directory in human readable format  
`ls -lah` - display all contents of current directory in human readable long list format  
`ls -t`  - sort contents by last time modified  
`ls -Glp` - display long list without group names and by appending '/' to directory names  

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

* `ls -Rl` - display list of subdirectories contents recursively
* `ls -lX` - list sorted by name alphabetically
* `ls -lS` - list sorted by file size
* `ls -lah` - long list of all files with human readable sizes
* `ls -lt` - list sorted by last time modified

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

`xargs` will start its own command line and can be used to run commands in parallel by piping input from one command 
to xargs. In the following example I will use xargs to open all files in the current path that have the **.py** extension:  

`find . -name "*.py" | xargs gedit`

 

