#               READING files
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



#A few fancy things are going on in this file, so let’s break it down real
#quickly:
#Lines 26-28 uses argv to get a filename. Next we have line 30, where we use a
#new command open. Right now, run pydoc open and read the instructions.
#Notice how, like your own scripts and input, it takes a parameter and returns
#a value you can set to your own variable. You just opened a file.

#Line 32 prints a little message, but on line 33 we have something very new and
#exciting. We call a function on txt named read. What you get back from
#open is a file, and it also has commands you can give it. You give a file a
#command by using the . (dot or period), the name of the command, and
#parameters, just like with open and input. The difference is that txt.read()
#says, “Hey txt! Do your read command with no parameters!”
#The remainder of the file is more of the same, but we’ll leave the analysis to
#you in the Study Drills.
#------------------------------------------
#           study drills
#------------------------------------------
#1. Above each line, write out in English what that line does.
#               done

#2. If you are not sure, ask someone for help or search online. Many times
#   searching for “python3.6 THING” will find answers to what that THING
#   does in Python. Try searching for “python3.6 open.”
#                   pass

#3. I used the word “commands” here, but commands are also called
#   “functions” and “methods.” You will learn about functions and methods later
#   in the book.
#               okay

#4. Get rid of the lines 10-15 where you use input and run the script again.
#           done

#5. Use only input and try the script that way. Why is one way of getting the
#   filename better than another?
#       When run that way, you dont have to input interestingly

#6. Start python3.6 to start the python3.6 shell, and use open from the prompt
#   just like in this program. Notice how you can open files and run read on them
#   from within python3.6?
#       see Above

#7. Have your script also call close() on the txt and txt_again variables. It’s
#   important to close files when you are done with them.
#       see above 
