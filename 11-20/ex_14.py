#               Excercise 14: Prompting and Passing
# Lets use argv and input together to ask the user something specific.
# you will need this for the next exercise where you learn to read and
# write files.

# were going to use input to print a simple prompt.

from sys import argv

script, user_name, adjective = argv
prmpt = '> '

print(f"Hi {adjective} {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {adjective} {user_name}?")
likes = input(prmpt)

print(f"Where do you live {adjective} {user_name}?")
lives = input(prmpt)

print("What kind of computer do you have?")
computer = input(prmpt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
#1. Find out what the games Zork and Adventure were. Try to find a copy and
#   play it.

#2. Change the prompt variable to something else entirely.
# changed to prmpt

#3. Add another argument and use it in your script, the same way you did in
#   the previous exercise with first, second = ARGV.
#           added adjective

#4. Make sure you understand how I combined a """ style multiline string
#   with the {} format activator as the last print
#       This was added to make a paragraph with formatted text
