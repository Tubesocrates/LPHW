#       exercise 30
# Else and if
print("This is the Study Drills from last session:")

quest_a = ["What do you think the 'if' does to the code under it?",
"Why does the code under the 'if need to be indented four spaces?",
"What happens if it isn't indented?",
"Can you put other boolean expressions fro Exercise 27 in the if-statement?",
"What happens if you change the initial calues for 'people, cats, and dogs'?"]

ans_a = ["""An if-statement
creates what is called a “branch” in the code. It’s kind of like those choose
your own adventure books where you are asked to turn to one page if you
make one choice and another if you go a different direction. The ifstatement
tells your script, “If this Boolean expression is True, then run the
code under it, otherwise skip it.
""",
"""A colon
at the end of a line is how you tell Python you are going to create a new
“block” of code, and then indenting four spaces tells Python what lines of
code are in that block. This is exactly the same thing you did when you made
functions in the first half of the book.
""",
"""If it isn’t indented, you will most likely
create a Python error. Python expects you to indent something after you end a
line with a : (colon).
""",
"""Try it. Yes you can, and they can be as complex as you like,
although really complex things generally are bad style.
""",
"""Because you are comparing numbers, if you change the numbers, different
if-statements will evaluate to True and the blocks of code under them will
run. Go back and put different numbers in and see if you can figure out in
your head which blocks of code will run.
"""]

#------------------   CODE  ----------------------------------
# p = [(a,b) for a in quest_a for b in ans_a]
i = 0
while i < len(ans_a):
    Q = quest_a[i]
    A = ans_a[i]
    print("%d. %s\n\n\t A. %s".replace('\t', " "* 2) \
        % (i, Q, A))
    i += 1

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we should take trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
