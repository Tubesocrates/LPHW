#Exercise 13. Parameters, Unpacking, variables
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

# 1. On line 11 we have an "import", this is how you add features to your Script
#    from the python feature set.
# 2. Rather than give you all the features at once, python wants you to say what
#    you will use to keep files small and acts as documentation for other
#    programmers who will read the code.

# 3. argv is the "argument variable.". This variable holds the arguements
#    you pass to your python script when you run it.

# 4, Line 3 unpacks argv so that, rather than holding all the arguements,
#    it gets assigned to four variables you can work with:
#           script
#           first
#           second
#           third
# it says "Take whatever is in argv, unpack it, and assign it to all of
# these variables on the left in order"


# after that we just print them like normal

# features have another name.
#       Modules
# other programmers call them libraries

# run the program with three command line arguements
#       Like This
#           python ex_13.py first 2nd 3rd
#
# you can actually replace first, 2nd and 3rd with anything.
