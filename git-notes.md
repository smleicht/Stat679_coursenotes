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

9/26/18 Wednesday 
deleting .git directory in a repository will remove the repository from the directory you are in.
need to `rm -f` to remove `.git` respository or you will be asked about deleting every single file

`git pull ` will pull new updates from githib.
`git clone` to create a new repository
`git merge` merges changes made to a single file being accessed by two or more people
`git remote -v` will say if you are currently connected to a remote repository
`git branch` will tell you what branch you are on

before pulling, always commit changes. Try to pull and new changes will erase wat you just tried to do, git won't let you do this.

`git merge` merge commit when two people are working on the same file at the same time
will need to manually resolve the conflicts. VS will show you the differences in the file and will ask whether you want to keep what you changed, what the other person changed, and overall how to resolve the conflict 

10/1/18 adding more notes for git homework due today before class. 

make shorter comments in scripts
comment that helps reader understand what is being done if it is not obvious
make sure to write out all assumptions that are being made as well
make a comment that explains what each variable means, write for humans what each variable means

cut is really cool
cut -f 1 will cut the first column
"f" is a field, can ask for multiple fields at once
-d will change the delimiter between column fields instead of tab, -d ' ' for a space
-d, -d , -d ',' will instert commas as a csv format, tab is deafult delimited


sort based on keys -k which are columns
n will sort things numerically but not as strings
-c just checks to see file is already sorted
change the delimited -t, tab is default delimiter(old school)

trying to sort columns that do not start with numbers, want to treat it like a string
r option will list things in decending order, if place with a key will only affect that one key, when -r will reverse 

`grep “ENSMUSG00000033793” Mus_musculus.GRCm38.75_chr1.gtf | cut -f 3 | sort | uniq`
in class exercise to search for genomic features associated with a gene 

column will make things look nice and -t will tab delimit the columns

sed substitute/this/bythat
what you want to look at and what you want to change it to.... always send it to a new file never send it to the same file
` sed 's/chrom/chr/'` will replace chrom by chr

capture things with parathenses, capture then and replace them with 

10/3/18
exercise 3 is due next wednesday at 8pm, then going to do peer review on each other's code due 10/15 (5 days later) 2 reviewers per code
do diff expected output vs output of what the person's code outputs out 

everyhting in parathenses is a subshell in a program

column -t will make the columns of the output nicer looking

`#!/bin/bash` says to use bash when executing this script, will run it in bash without saying bash

set settings in beginning of script will make script more safe
error  occurs, stop command



./ will say in this directory, but will not allow to just run scripts 

tell if directory or file, rwe (read, write, execute) - means you dont have permission
first grouping- owner
people in a group what they can do
everyone who could ever access file

chmod-chnage modify u (user) +x (to execute)
add permission for yourself to execute a file

bin needs binary, executable scripts

export PATH="$PATH:~/bin", adding to the path variable, will have things that were in there beforehand

(()) tells the shell that some arithmetic is going to be done

if this is true, do this
can have else if what is not true
then fi to end the if statement

-lt (less than)

-o is or within an if statement, if find that first statement in if statement then stops looking, will only look at a will not look at b

10/8/18 Git branches
bare respository only has .git folder, no files in this respository. just .git

branches are convienent to develop something you dont want anyone to see 
git branch "branch name" creates a new branch 
git branch will list the branches you have and a * will show which branch you are on

-d option will delete a branch 

 will list history of a repository in one line, and show graph of branches

branches do not contain information, commits do

git branch -vv verbose will show chnages to branches

git fetch --all will get all things that are new, not just what is changed on the branch you are currently on

git checkout to a previous commit will show you what information was that commit, when git checkout from current commit then you will get to that commit

checkout is liek cd in git

git checkout master
git merge readme-changes

will merge readme-changes branch to the master branch

branch -a will list all branches

when merging, want to be on the branch that will have the change

git fetch --prune will get deletions as well as additions

git commit --amend will chnage message involved in the commit
 
shasum
0 or 1 is a bit
1 byte = 8 bits
1 nibble = 4 bits

0000 = 0
0001 = 1
0010 = 2
...
1111 = 15


nibble 16 base
0 1 2 .... 8 9 a(10) b(11) c(12) d(13) e(14) f(15)
8 = 1000
each character is 4 bits, a nibble

used when downloading software use shasum to make sure softward hasnt been corrupted by viruses

10/10/18 wednesday
awk is a text editor, sed is a stream editor (awk is considered to be a stream editor as well)
more powerful than sed
takes input file or standard input
tell awk an pattern and {action} within the brackets
can have awk statements that have patterns, some that only have action, and some that have both
!= not &&= and ||= or
if no action, print the entire line. $1, $2 are specific variables 
field is a column within a line, record is a line number
== is to test
awk is kind of a programming langauge on its own
awk works on tabular data, default delimiter is tab, -F"," will change the field/delimiter to a , for a csv file

awk '$3 - $2 > 18' example.bed will print lines that follow this pattern only, third column minus the second column is equal to 18

chr2|chr3 means matches chr2 or chr3, matches one or the other

{ s = 0 }; { s += ($3-$2) defines a variable and then adds the difference between columns 3 and 2 to the value s
NR is total number of records that you have read so far

[] is an array

feature[$3]+= 1
feature[gene]+= 1, associative array
associate a key that is not necessarily a number to a value and += will increment by 1
feature
gene --> 1
transcript --> 1
exon --> 1
gene --> 2 ( when comes up again in a file)

transcript, gene, exons are keys in awk

# will have you strip things from the beginning of the name of something
wget- will get data from the internet

curl will redirect things as standard output, would 

10/22/18 Monday intro to Python

integer vs floating value
integer is compatible with bits in coding language (64 bit notation)

floating value = 1.234567 or 12.34567
use scienitifc notation in this case 
1.234 * 10^102 0r 1.234 * 10^-102 for writing really large or really small numbers
both of these numbers are 11 bits (one bit for the sign of the exponenet)

Integers are fundamentally different from floating values

booleans= 0 is false, 1 is true
bool(1.3) is True

float(True)= 1      bool(None)= False

good for if statements for returning true or false statements 

1.0/3.0 == 1.0 - 2.0/3.0  is asking 1/3 equal to 1-2/3
but python says False, because floating values will cause numerical calculation errors

"%s %s hello %s" will help you write strings of numbers and not the bits of the numbers

% is a string, s is a space

%d will print numbers are integers even if they are floating values 

%.2f writing a float with two values after the decimal place

%.1e will write a numver is scientific notation 

[10,20] is a list  (10,20) is a tuple

we can change lists but not tuples

mutables vs immutables
mutable means you have the ability to change something 
strings are immutable, so are tuples, floats, and booleans

lists of lists is not the same thing as an array

have lists within lists that depend on each other, if change a value within the list, one of the values on the "outside" of the list will be chnaged if an interior value is changed
lists are mutable

deep copy vs simple copy
when making a copy of lists if lists, even if make a copy and then chnage a value in the list it will chnage what is in the list even though a copy has been made

ex. a = [[10,11].[20,21]]
b = copy.copy(a)
b[0][0] = 50
this chnages both a and b

but if 
a = [[10,11].[20,21]]
b = copy.deepcopy(a)
b[0][0] = 8
will chnage without affecting a

functions is similar to writing for loops
def add1_scalar(x):
    """adds 1 to scalar input"""
    x += 1
    print("after add1_scalar:", x)

like for loops, defining functions end when indentation goes away 


within a session you have defined variables and names, when writing a function you can copy variables into functions and original list is unchanged when function is executed

but can write a function to make a value within a session to make it mutable, function can chnage it 

split will operate on strings give it some sort of delimiter, split with a space or a comma or whatever

replace something with something else, 

\n for new line, \t for a tab

strip will get rid of extra spaces
rstrip will strip what is on rhe righthand side