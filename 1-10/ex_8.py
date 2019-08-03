# This is the thing being formatted
# "{}" is being replaced with whatever I format into it

formatter = ("{}"
            " {}"
            " {}"
            " {}")

# below prints 1, 2, 3 and 4 into "formatter"
print(formatter.format(1, 2, 3, 4))
# same as above but with words
# notice this has to take strings
print(formatter.format("one", "two", "three", "four"))
# here takes the boolean value of true and false
print(formatter.format(True, False, False, True))
# here is a nexted function putting formatter into itself
# recursivity
print(formatter.format(formatter, formatter, formatter, formatter))
# interestingly the enter-indent doesnt affect the code remotely
# this just makes a conjoined text string
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))
