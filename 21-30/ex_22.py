## REVIEW:

#       printing 1,2
print("Hello World!")
#------------------------------------------------------
#------------------------------------------------------
#       math truth, floats, round
#       3, 4, 5
print("Is is true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)
space_in_a_car = 4.0
sce = round(space_in_a_car)
#------------------------------------------------------
#------------------------------------------------------
#      6,7, formatting
# f-string = f""
# format = .format()

# value setting binary and do_not
binary = "binary"
do_not = "don't"
# variables of the formatted variety
# This assigns "Those who know binary and those who don't." to y
y = f"Those who know {binary} and those who {do_not}."

# value setting for hilarious and joke_evaluation
hilarious = False
# here I create a possibility of this string to be formatted
# without pre-formatting
joke_evaluation = "Isn't that joke so funny?! {}"

#we are formatting the string with this formatting operator
# it formats the string "joke_evaluation" with inserting hilarious
x = joke_evaluation.format(hilarious)
z = "."*10
print(y, z,  x, end = ' ')
#------------------------------------------------------
#------------------------------------------------------
# combining and multiplying strings
formatter = "{} {} {} {}"
print(formatter.format(formatter, formatter, formatter, formatter))

# this just makes a conjoined text string
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
#------------------------------------------------------
#------------------------------------------------------
#      10, formatting
# escape double-quotes
# examples

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """

I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
#------------------------------------------------------
#------------------------------------------------------
#      11, input
print("How old are you?", end=' ')
# we put a "end=' '" at the end of each print line. This tells print to not
# end the line with a newline character and go to the next line
# for the input function we need to run in powershell
# cd LPHW
# python ex_11.py
# the input function allows user input

age= input()

print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
#------------------------------------------------------
#------------------------------------------------------
#      12, input

#Prompting People
# When you type input you type (), the parenthesis characters
# This is similar to when you used them to do a format with extra variables
# as in f"{x} {y}". For input you can also put in a prompt to show a person
# so they know a type. Put a String that you ant for the prompt inside the ()
# so that it looks like this:
#    y = input("Name?")

# This prompts the user with "Name?" and puts the result into the variable y.

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#Study Drills
# 1. type python -m pydoc ex_12
# 2. type python -m pydoc input
#         this will tell you what input does
# use pydoc to read about open file os and sys
# 3. type python -m pydoc XXXXX
#------------------------------------------------------
#------------------------------------------------------
#           Exercise 13. Parameters, Unpacking, variables

# In this exercise we will cover one more input method you can use to pass
# variables to a script. (Script being another name for .py files)
# when in terminal we type python ex_13.py. the ex_13.py part of the
# command is called an "argument".
# were going to write a script that also accepts arguements.

#------------------------------
#          CODE
#-----------------------------
from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
fourth_variable = input("What is your fourth variable? ")
print(f"Ah, okay. So your Variables are {first}, {second}, {third} and {fourth_variable}")

#------------------------------------------------------
#------------------------------------------------------
#               Excercise 14: Prompting and Passing
# Lets use argv and input together to ask the user something specific.
# you will need this for the next exercise where you learn to read and
# write files.

# were going to use input to print a simple prompt.

from sys import argv

script, user_name, adjective = argv
prmpt = '> '

print(f"Hi {adjective} {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {adjective} {user_name}?")
likes = input(prmpt)

print(f"Where do you live {adjective} {user_name}?")
lives = input(prmpt)

print("What kind of computer do you have?")
computer = input(prmpt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
#------------------------------------------------------
#------------------------------------------------------
#               Excercise 15: Reading Files

#You know how to get input from a user with input or argv. Now you will
#learn about reading from a file. You may have to play with this exercise the
#most to understand what’s going on, so do the exercise carefully and
#remember your checks. Working with files is an easy way to erase your work
#if you are not careful.

#This exercise involves writing two files. One is the usual ex15.py file that
#you will run, but the other is named ex15_sample.txt. This second file isn’t
#a script but a plain text file we’ll be reading in our script. Here are the
#contents of that file:
#   This is stuff I typed into a file.
#   It is really cool stuff.
#   Lots and lots of fun to have in here.

#What we want to do is “open” that file in our script and print it out. However,
#we do not want to just “hard code” the name ex15_sample.txt into our
#script. “Hard coding” means putting some bit of information that should
#come from the user as a string directly in our source code. That’s bad because
#we want it to load other files later. The solution is to use argv or input to ask
#the user what file to open instead of “hard coding” the file’s name.

#------------------------------------------
#           code
#------------------------------------------
# here i am imprting the module argv from the library sys
from sys import argv
#here i define my arguments to call later in the script
#script, filename = argv
#---------------------
#       6
script = argv
filename = "ex_15_sample.txt"
txt = open(filename)
#------------------------
# i am defining a new variable with the function open which is in default r mode to read the
# text that i give it use pydoc to learn more about open.
##txt = open(filename)
# here i have a formatted statement that calls the filename provided
print(f"Here's your file {filename}:")
#here we call on the read function to read the txt variable that we defined above,
#then we print it
print(txt.read())
#-----------
#     7
txt.close()
#here we have more text printed
#           Unhash for more fun
print("Type the filename again:")
#define our input with a variable
file_again = input("> ")
#now we define a variable be equal to the variable above defined at input to be opened by the
# function
txt_again = open(file_again)
#then finially we print the last defined variable while using the read function to read it
print(txt_again.read())
#-----------
#     7
txt_again.close()
#------------------------------------------------------
#------------------------------------------------------
#               Excercise 16: Text Editor

 #List of commpands.
#• close – Closes the file. Like File->Save.. in your editor.
#• read – Reads the contents of the file. You can assign the result to a variable.
#• readline – Reads just one line of a text file.
#• truncate – Empties the file. Watch out if you care about the file.
#• write('stuff') – Writes “stuff” to the file.
#• seek(0) – Move the read/write location to the beginning of the file.

#One way to remember what each of these does is to think of a vinyl record,
#cassette tape, VHS tape, DVD, or CD player. In the early days of computers
#data was stored on each of these kinds of media, so many of the file
#operations still resemble a storage system that is linear. Tape and DVD drives
#need to “seek” a specific spot, and then you can read or write at that spot.
#Today we have operating systems and storage media that blur the lines
#between random access memory and disk drives, but we still use the older
#idea of a linear tape with a read/write head that must be moved.

#For now, these are the important commands you need to know. Some of them
#take parameters, but we do not really care about that. You only need to
#remember that write takes a parameter of a string you want to write to the
#file.

#Let’s use some of this to make a simple little text editor:

from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you dont want that, hit CTRL-C (^C) .")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# 'w' stands for writing permission for the opened file, you are calling it with the purpose
# or writing to it
target = open(filename, "w")


print("Truncating the file. Goodbye!")
#truncate empties the file
target.truncate()

print("Now I'm going to ask you for three lines.")
textlist = []
line1 = input("line 1: ")
textlist.append(line1)
line2 = input("line 2: ")
textlist.append(line2)
line3 = input("line 3: ")
textlist.append(line3)


print("I'm going to write these to the file.")
#below writes the three lines to our file
#before study drill 3
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#after study drill 3 this adds more lines
print("Lets double those lines.")
#old write COde, adds unnecessary strings
#target.write('%r\n%r\n%r\n' % (line1, line2, line3))

#new write code
for line in textlist:
  # write line to output file
  target.write(line)
  target.write("\n")
target.close()
#study drill number 2
# i had to close and then open the file to properly read the file. interesting

r_target = open(filename)
read = (r_target.read())


print(f"This is the newly formatted {filename}.")
print(read)
r_target.close()

#r_target2 = open(filename)
#filepath = 'text.py'
with open(filename) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1
#read2 = (r_target2.readline(2))
#print("Line 2 is:", read2)

print("And finally, we close it.")
#this closes the in-use file
target.close()


#------------------------------------------------------
#------------------------------------------------------
#               Excercise 17: Copying one file to another

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# 1 Make this easier to use
# 2 make this one line long
#from sys import argv; open(to_file, "w").write(open(from_file).read())

##print(f"Copying from {from_file} to {to_file}")

# we combined these two on one line, how?
##in_file = open(from_file)
##indata = in_file.read()
#   indata = open(from_file).read()

##print(f"The input file is {len(indata)} bytes long")

##print(f"Does the output file exist? {exists(to_file)}")
##print("Ready, hit RETURN to continue, CTRL-C to abort.")
##input()

##out_file = open(to_file, "w")
##out_file.write(indata)

##print("Alright, all done.")

##out_file.close()
##in_file.close()

#*******in powershell******
#use echo "Put new text in here."> thenewfilesname.Here
#then use cat to read it

#1. This script is really annoying. There’s no need to ask you before doing the
#   copy, and it prints too much out to the screen. Try to make the script more
#   friendly to use by removing features.
#2. See how short you can make the script. I could make this one line long.
#3. Notice at the end of the What You Should See I used something called cat?
#   It’s an old command that “con*cat*enates” files together, but mostly it’s just
#   an easy way to print a file to the screen. Type man cat to read about it.
#   4. Find out why you had to write out_file.close() in the code.
#       https://stackoverflow.com/questions/36046167/is-there-a-need-to-close-files-that-have-no-reference-to-them/36063184#36063184
#   5. Go read up on Python’s import statement, and start python3.6 to try it out.
#   Try importing some things and see if you can get it right. It’s alright if you do
#   not.


#------------------------------------------------------
#------------------------------------------------------
#               Excercise 18: Using and formatting Arguments,
#                   Names, Variables, Code, Functions
# this is like one of your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do This
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I've got nothin'.")

print_two("Josh","Johnson")
print_two_again("Jibby", "Johnson")
print_one("Second!")
print_none()

#Let's break down the first function, print_two, which is the most similar to
#what you already know from making scripts:
#1. First we tell Python we want to make a function using def for "define".
#2. On the same line as def we give the function a name. In this case we just
#   called it "print_two," but it could also be "peanuts." It doesn't matter, except
#   that your function should have a short name that says what it does.
#3. Then we tell it we want *args (asterisk args), which is a lot like your argv
#   parameter but for functions. This has to go inside () parentheses to work.
#4. Then we end this line with a : (colon) and start indenting.
#5. After the colon all the lines that are indented four spaces will become
#   attached to this name, print_two. Our first indented line is one that unpacks
#   the arguments, the same as with your scripts.
#6. To demonstrate how it works we print these arguments out, just like we
#   would in a script.

#The problem with print_two is that it's not the easiest way to make a
#function. In Python we can skip the whole unpacking arguments and just use
#the names we want right inside (). That's what print_two_again does.
#After that you have an example of how you make a function that takes one
#argument in print_one.
#Finally you have a function that has no arguments in print_none.

#What does the * in *args do? That tells Python to take all the arguments to
#the function and then put them in args as a list. It's like argv that you've been
#using but for functions. It's not normally used too often unless specifically
#needed.
#------------------------------------------------------
#------------------------------------------------------
#               Excercise 19: Functions, Variables and Math

#19 functions and variables
#There is one tiny point that you might not have realized, which we’ll
#reinforce right now. The variables in your function are not connected to the
#variables in your script. Here’s an exercise to get you thinking about this:

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

print("We can just give the function numbers directly:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do the math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers*5)

#------------------------------------------------------
#------------------------------------------------------
#               Excercise 20: Functions, Reading files and lines

#        ctrl + / for commenting out blocks of code
# Remember your checklist for functions, then do this exercise paying close
# attention to how functions and files can work together to make useful stuff.
from sys import argv
script, input_file = argv

#           functions

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

# def print_a_line(f):
#     print(f.readline(f))

#           variables
current_file = open(input_file, "r")
#           code
print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:\n")
count = 1
for lin in current_file.readlines():
    count +=1
    print(str(int(count - 1)),lin, end = "")
# object names
print("\nAgain:\n")

with open(f"{input_file}") as f:
    for p in f:
        print(p)

#                               Study Drills
# 1. Write English comments for each line to understand what that line does.
# 2. Each time print_a_line is run, you are passing in a variable
#    current_line. Write out what current_line is equal to on each function
#    call, and trace how it becomes line_count in print_a_line.
# 3. Find each place a function is used, and check its def to make sure that you
#    are giving it the right arguments.
# 4. Research online what the seek function for file does. Try pydoc file,
#    and see if you can figure it out from there. Then try pydoc file.seek to see
#    what seek does.
# 5. Research the shorthand notation +=, and rewrite the script to use += instead.

#------------------------------------------------------
#------------------------------------------------------
#               Excercise 21: Math
string = ""

def add(a, b):
    print(f"Adding: {a} + {b}")
    #string += a + b
    return a + b


def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    #string += a - b
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    #string += a * b
    return a * b

def divide(a, b):
    print(f"Dividing {a}/{b}")
    #string += a / b
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")

print(f"{age} + ({height} - ({weight} * ({iq}/2))) =", str(what))


# Study Drills
# 1. If you aren’t really sure what return does, try writing a few of your own
#    functions and have them return some values. You can return anything that
#    you can put to the right of an =.
#               skip
# 2. At the end of the script is a puzzle. I’m taking the return value of one
#    function and using it as the argument of another function. I’m doing this in a
#    chain so that I’m kind of creating a formula using the functions. It looks
#    really weird, but if you run the script, you can see the results. What you
#    should do is try to figure out the normal formula that would recreate this
#    same set of operations.
#              done
# 3. Once you have the formula worked out for the puzzle, get in there and see
#    what happens when you modify the parts of the functions. Try to change it on
#    purpose to make another value.
#               skip
# 4. Do the inverse. Write a simple formula and use the functions in the same
#    way to calculate it.
#    This exercise might really whack your brain out, but take it slow and easy
#    and treat it like a little game. Figuring out puzzles like this is what makes
#    programming fun, so I’ll be giving you more little problems like this as we
#    go.
#               skip
