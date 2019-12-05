# IMPORT
from sys import exit
from pprint import pprint
# pyowm = python wrapper for weather app
# https://github.com/csparpa/pyowm
import pyowm
from datetime import datetime


#-------------------------------------------------------
#                   Keywords
#-------------------------------------------------------

print("***AND***")
#and
x = 3
y = 4
if x and y < 6:
    print("If x and y are less than 6 they are...",x,y)

print("***AS***")
print("***with***"")
#as <- attributing value
with o(sss.py) as f:
    f.read()

#assert <-
#   Assertions are simply boolean expressions that checks if the conditions return true or not.
#   If it is true, the program does nothing and move to the next line of code.
#   However, if it's false, the program stops and throws an error.

print("***DEF()***")
#   def a function
def o(y):
    assert open(y), "File not found"
    return open(y)


print("***BREAK***")
#break <- terminates the nearest enclosing loop skipping the optional else clause if the loop has one
# Use of break statement inside loop

for val in "string":
    print("this function will break before i.")
    if val == "i":
        break
    print(val)

print("The end")

print("***CLASS***")
#class
class Dog:
    kind = 'canine' #variable shared by all in the class

    def __init__(self, name, breed, weight):
        self.name = name
        self.breed = breed
        self.weight = weight
d = Dog('Fido', 'Chiuaua', "145 kg")
m = Dog('Spot', 'Bulldog', "5 kg")

print(d.name, d.breed, d.weight)
print(m.name, m.breed, m.weight)

print("***CONTINUE***")
print("***FOR***")
print("***IS***")
print('***NOT***')
print('***OR***')
print('***PASS***')
print('***PRINT***')
print("***while***"")
#continue <- dont process more of the loop do it again
for letter in 'Python':     # First Example
   if letter is 'h':
      continue
   print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:
    var = var -1
    if var == 5 or not < 1:
        continue
    elif var > 9:
        print('pass')
        pass

    print 'Current variable value :', var
print "Good bye!"

print("***DELETE***")
# del <- delete from a dictionary or list

l = ["apple", "banana", "cherry"]
print("l =", l)
del x[0]
print("now l =", l)
#The del statement removes an element:

# del d[key]
# However, this mutates the existing dictionary so the contents of the dictionary changes for anybody else who has a reference to the same instance. To return a new dictionary, make a copy of the dictionary:
#
# def removekey(d, key):
#     r = dict(d)
#     del r[key]
#     return r
# The dict() constructor makes a shallow copy. To make a deep copy, see the copy module.
but = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
}

print("but =", but)


print("***elif***")
print("***else***")
print("***if***")

print("How do you feel?")
input = ("> ")

if len(input) < 5:
    print("You can gimme a longer answer than that.")

elif len(input) > 20:
    print("Jeez, you ever shut up?")

else:
    print("Ah, I get you.")


print("***except***")

print("""
The windows_interaction() can only run on a Linux system.
The assert in this function will throw an AssertionError exception if you call it on an operating system other then Linux.
""")

def windows_interaction():
    assert ('windows' in sys.platform), "Function can only run on windoes systems."
    print('Doing something.')

try:
    windows_interaction()
except:
    "No windows, hmmm. How will you get fresh air? Get a PC comrade."
    pass

print("***exec***")
print("'Run a string as Python.'")

program = input('Enter a program:')
exec(program)
print("""
Here for example you can type:
[print(item for item in [1, 2, 3])]
""")

print("***finally***"")
print("***try***"")
print("Eceptions or not, finally do this no matter what.")

print("Lets try our new divide function.")

print("Lets divide 3 and 0")
def divide(x, y):
     try:
         result = x / y
     except ZeroDivisionError:
         print("division by zero!")
     else:
         print("result is", result)
     finally:
         print("executing finally clause")
divide(3, 0)
print("Now lets divide 4 and 2")
divide(4, 2)

print("***Global***"")
# tHIS FUNCTION SHOWS HOW THE GLOBAL VARIABLE changes
def foo():
    x = 20

    def bar():
        global x
        x += 25

    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main : ", x)


print("***lambda***"")
# In Python, anonymous function means that a function is without a name.
#As we already know that def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.
#It has the following syntax:
# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y*y*y;

g = lambda x: x*x*x
print(g(7))

print(cube(5))
# more on lambda
#   https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/


print("***RAISE***"")
# THE RAISE STATEMENT ALLOWS THE PROGRAMMER TO FORCE A SPECIFIED EXCEPTION TO OCCUR
# WILL NOT MAE A RASIE DFUNCTION DUE TO IT BEING SOMETHING THAT ONE SHOULDNT DO
print("***RETURN***"")
def greater_than_1(n):
    return n > 1

print("***Yield id very confusing google it!!")


#-------------------------------------------------------
#                   Data Types
#-------------------------------------------------------

print("True, False")

print("True or Flase??")
input = ("> ")

if input == True:
    print("Nah, flase")

elif input == False:
    print("YEEEE")

else:
    print("okay...")

print("None")
