#           Loops and Lists
# Things List can do:
# .append - adds on to the list one element at a time
#       for addition of multiple elements use loops
#       we can alos add tuples because they are immutable
#       we can also add lists
#       This only works for the addition of elements at the end of a list
# .insert(position, value) - insets values at given positions, this method requires two inputs
# .extend() - this mehtod is used for adding multiple elements at the same time at the end of the list
# .remove() - remove method only removes one element at a time, to remove ranges use iterator
# .pop(position) can be used to remove and return an element for the set, but by default it removes the last element of the set
#        place a position in the .pop() method to remove anything at that value.
# slicing - use google to find the rest

# You should now be able to do some programs that are much more interesting.
# If you have been keeping up, you should realize that now you can combine
# all the other things you have learned with if-statements and boolean
# expressions to make your programs do smart things.

# However, programs also need to do repetitive things very quickly. We are
# going to use a for-loop in this exercise to build and print various lists. When
# you do the exercise, you will start to figure out what they are. I won’t tell you
# right now. You have to figure it out.

# Before you can use a for-loop, you need a way to store the results of loops
# somewhere. The best way to do this is with lists. Lists are exactly what
# their name says: a container of things that are organized in order from first to
# last. It’s not complicated; you just have to learn a new syntax. First, there’s
# how you make lists:

# hairs = ['brown', 'blond', 'red']
# eyes = ['brown', 'blue', 'green']
# weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count: {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts\
# 1.  look up range function
#           i know how to use range
# can you avoid the range function entirely and just assign range(0, 6) directly to elements?
x = range(0, 7)
print("List_X =", list(x))

for i in range (0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand and adds on the end of them
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")


# How do you make a 2-dimensional (2D) list? That’s a list in a list like this:
# [[1,2,3],[4,5,6]]

# Aren’t lists and arrays the same thing? Depends on the language and the
# implementation. In classic terms a list is very different from an array because
# of how they’re implemented. In Ruby though they call these arrays. In
# Python they call them lists. Just call these lists for now since that’s what
# Python calls them.

# Why is a for-loop able to use a variable that isn’t defined yet? The
# variable is defined by the for-loop when it starts, initializing it to the current
# element of the loop iteration each time through.

# Why does for i in range(1, 3): only loop two times instead of three
# times? The range() function only does numbers from the first to the last, not
# including the last. So it stops at two, not three in the preceding. This turns out
# to be the most common way to do this kind of loop.

# What does elements.append() do? It simply appends to the end of the list.
# Open up the Python shell and try a few examples with a list you make. Any
# time you run into things like this, always try to play with them interactively
# in the Python shell.
