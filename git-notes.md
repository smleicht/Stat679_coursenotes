Stat 679 9/5/18 Wednesday
Write code for humans, data for computers
use multiple assertions to test out a piece of code (example on notes on GitHub page for 9/5/18)
A variable is name that contains a value

For homework: start software carpentry, check GitHub, and go through navigating files and directories

9/10/18 Monday
Uses .. and / are relative paths
Users/Amanda/data is an absolute path

Relative paths are better because if you move directories then the absolute paths changes. Relative paths are more portable

Cd - will get you back to where you were before, not “up” a directory 

Raw sequences = raw\ sequences. “\” escapes the space

Ls a directory it will tell you whats in the directory, not the name of the directory. Ls r* will list whats in directories that start with r, not directories that start with r

9/12 Wednesday 
Run a program with a lot of output on to screen can redirect the output to dev/null/  which is the garbage with a carrot so don’t see it on your screen

Can pause a program with ctrl Z and can restart in the foreground fg or background bg
Running things in the background allows you to still use your shell

Ps shows processes that are going on, shows a process ID (PID)

Kill and a number -1 to -9 where 9 is the strongest, will end jobs

Run a program and type & at the end of it, sends command to background automatically 

Search through a list of things that is very long using command grep

9/17/18 Monday
Less reads beginning of file as a small stream
Quit to get out of it
More looks the same as less, but can click space to see more and more and more of the file

Less is better, can search through it 
In less, can type G and get to the end of the file g will get to the top of the file

Man ls will have you see less of a manual
 / within less will allow you to search within a file
N gives you next search item in file
?itemsearching will get you last item in search list

Grep to find things inside of files, content
Find searching file names

When type a wildcard, the shell expands * first
With quotes around it, shell will not expand it
Environmental variables will be expanded by the shell
Single quotes are protective, nothing will expand within the single quotes
$( means run this command

-o will get the match only ONLY
-v inverts the search
-d is depth, for how far into a directory we want to go in

Xargs, what I am going to give you is the filename, not the content

Put single quotes around a variable, shell won’t touch it and expand it first, put it in single quotes and find all files that end in .txt even if in a different directory

Need to tell the command that what you are input are arguments, not the inputs

Installed GNU via home-brew, to use GNU version of commands, use gcat and ggrep

Shell
*= anything, any length
? = 1 character
.=.

Regular expression
.= any one character
^ is a boundary
\ turns off special meaning of a system
\w any word character, a letter, a number, _ no ., no -
No word \W

[[:alnum:]]
Outer brackets, this or or or or
Inner brackets mean any number or letter

\d any single digit [0-9] is numbers 0 to 9
:predefined category:

Carriage return- move to front of the paper in type writer
\s empty space

\d* \.  \d+     find zero or more digits and a dot and another digit on or more

\d* [\.] \d+ would find a digit, with dot or comma in center and then has one more digit

Exclude first line of a file, starts with >, all fasta files start with >

Grep -v “^>” tb1.fasta | less
carrot indicates that its the beginning of the line, pipe to less to see that so far this is what we want to do

Grep -v “^>” tb1.fasta | grep [^ACGTacgt] | less
 
Couldn’t see it, so colored it
 Grep -v “^>” tb1.fasta | grep —color [^ACGTacgt] 

Want to only see what is not wrong
 Grep -v “^>” tb1.fasta | grep -on [^ACGTacgt]

-I is case insensitive 

9/19/18 Wednesday
Use relative paths in scripts so that a collaborators can use scripts
Tell collaborator where all files are in one directory and tell them to navigate within the same directory within everything

Document in a readme file
“Run script by going into x file and running this command. It assumes that you have this type of input and will give you this type of out file” 
More high level than comments within the script
Code, meaning, code, meaning

Comments go inside the script of what exactly the script is doing, more details.

-mtime will tell last time a file was modified -1 would tell you it was modified a day ago.

^ not at beginning will just be a carrot, just searching for the character
^ means search the beginning of a line
When there is a match grep shows us the entire line, maybe don’t want entire line
-o will only show what has been searched for
 
In find -d is depth, only go down # of steps 

Use xargs when pipe shouldn’t take the content but the arguments from the previous command

Touch to make a file

Md is markdown, simple text

Git is a good place to store code, not data
Use plain text file because can be searched easily, small, light, text can always be read. 

9/24/18 Monday
Quicker and half-assed may be better at times to tell you communicate with you collaborators 

Git takes snapshots of project, and can go back to any of them at any time

Using text and short lines are key to making git efficient

Everything git does is store is special hidden git directory, .git, can only see it is ls -a to see all files

Can communicate with someone else using GitHub to save files/programs in an external repository. Can push things to github and pull things out of GitHub

Each time take a snapshot, write a reminder to say what each commit/change was. Each commit comes with special address

Can look through commits in GitHub to look for versions of documentation/code, go back to all previous  versions. 

Git init will create blank git repository, everything inside that folder you do this command in, will be saved to git

Git status does nothing, tells us things we may want to do. Tells you what you have committed, but tells you things you may want to commit, will also tell you when you make your next commit, what it will track

Git commit takes pictures. Have previous files, previous commits, have staging area where git knows a change has been made, takes intermediate snapshot, working files may be different from staging area files

Git diff shows me difference between any files that has changed without being committed.
To see difference from staged file and the previous commit= git diff —staged

-m in commit leaves a message for the commit

Can create branches from a master 

Commit opens text editor to write a message and extra paragraph to tell you everything that was changed in this version. Be descriptive and concise, be helpful to your future self/collaborators

Git show will show contents of commits, last one you made, can also take “address” and write git show and show the changes made in that specific commit

Git log shows title of commits, not the contents, will show who made the commit

git commit -a, will stage all files that have been changed, does both git add and git commit, will only do git add or git commit on the things you are tracking

adding another line because recap homework told me to do so.
Adding another with more capitalization and saying something about how I think git is super cool. 