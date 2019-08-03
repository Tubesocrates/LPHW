print("How old are you?", end=' ')
# we put a "end=' '" at the end of each print line. This tells print to not
# end the line with a newline character and go to the next line
# for the input function we need to run in powershell
# cd LPHW
# python ex_11.py
# the input function allows user input

age= input()

print("How tall are you?")
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
