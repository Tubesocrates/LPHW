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
