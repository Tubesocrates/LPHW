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
