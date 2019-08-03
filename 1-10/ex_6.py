# f-string = f""
# format = .format()-------- Line 17
#------------

# value setting of types_of_people
types_of_people = 10
# variables of the formatted variety
# this assigns "There are 10 types of people." to x
x = f"There are {types_of_people} types of people."

# value setting binary and do_not
binary = "binary"
do_not = "don't"
# variables of the formatted variety
# This assigns "Those who know binary and those who don't." to y
y = f"Those who know {binary} and those who {do_not}."

#------------------------------------------------------
# below are all examples of valid prints
# below print pre-formatted values with stored strings
print(x)
print(y)

# here we are formatting pre-formatted strings
# below prints "I said: There are 10 types of people."
print(f"I said: {x}")
# this next one is tricky its a quote inside a quote
# below prints "I also said: 'Those who know binary and those who don't.'"
print(f"I also said: '{y}'")

#------------------------------------------------------
# value setting for hilarious and joke_evaluation
hilarious = False
# here I create a possibility of this string to be formatted
# without pre-formatting
joke_evaluation = "Isn't that joke so funny?! {}"

#we are formatting the string with this formatting operator
# it formats the string "joke_evaluation" with inserting hilarious
print(joke_evaluation.format(hilarious))

#------------------------------------------------------
# value setting with the below strings
w = "This is the left side of..."
e = "a sting with a right side."
# here we are preforming string addition

print(w + e)
