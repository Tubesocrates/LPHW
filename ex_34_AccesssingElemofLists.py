# Lists are pretty useful, but unless you can get at the things in them they aren’t
# all that good. You can already go through the elements of a list in order, but
# what if you want say, the fifth element? You need to know how to access the
# elements of a list. Here’s how you would access the first element of a list:
#
# animals = ['bear', 'tiger', 'penguin', 'zebra']
# bear = animals[0]

# Programmers, however, can’t think this way because they can pick any
# element out of a list at any point. To programmers, the list of animals is more
# like a deck of cards. If they want the tiger, they grab it. If they want the zebra,
# they can take it too. This need to pull elements out of lists at random means
# that they need a way to indicate elements consistently by an address, or an
# “index,” and the best way to do that is to start the indices at 0. Trust me on
# this: the math is way easier for these kinds of accesses. This kind of number
# is a “cardinal” number and means you can pick at random, so there needs to
# be a 0 element.

# Let’s practice this. Take this list of animals, and follow the exercises where I
# tell you to write down what animal you get for that ordinal or cardinal
# number. Remember, if I say “first,” “second,” then I’m using ordinal, so
# subtract 1. If I give you cardinal (like “The animal at 1”), then use it directly.

# animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

# 1. The animal at 1. - 'python3.6'
# 2. The third (3rd) animal. - 'peacock'
# 3. The first (1st) animal. - 'bear'
# 4. The animal at 3. - 'kangaroo'
# 5. The fifth (5th) animal. - 'whale'
# 6. The animal at 2. - 'peacock'
# 7. The sixth (6th) animal. - 'platypus'
# 8. The animal at 4. - 'whale'

# For each of these, write out a full sentence of the form: “The first (1st) animal
# is at 0 and is a bear.” Then say it backwards: “The animal at 0 is the 1st
# animal and is a bear.”
# Use your Python to check your answers.

# Study Drills
# 1. With what you know of the difference between these types of numbers, can
# you explain why the year 2010 in “January 1, 2010,” really is 2010 and not
# 2009? (Hint: you can’t pick years at random.)
# 2. Write some more lists and work out similar indexes until you can translate
# them.
# 3. Use Python to check your answers.
