#       Exercise 31
#       Making Decisions

#
# In the first half of this book you mostly just printed out things called
# functions, but everything was basically in a straight line. Your scripts ran
# starting at the top and went to the bottom where they ended. If you made a
# function, you could run that function later, but it still didn’t have the kind of
# branching you need to really make decisions. Now that you have if, else,
# and elif you can start to make scripts that decide things.
# In the last script you wrote out a simple set of tests asking some questions. In
# this script you will ask the user questions and make decisions based on their
# answers. Write this script, and then play with it quite a lot to figure it out.


print("""You enter a dark room with three doors.
Do you go throgh door #1, door #2, or door #3?""")

door = input("> ")

if door == "1":
    print("there's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("the bear eats your face off. Good job!")
    elif bear == "2":
        print("the bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthlhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("This door is locked with a magical spell. to open it you need to guess a riddle. Do you want to try? yes/no")

    answer = input("> ")

    if answer == "yes":
        print("'The man who invented it doesnt want it. Th man who bought it doesn't need it. The man who needs it doesn't know it'. What is it?")

        riddle_ans = input("> ")

        if riddle_ans == "a coffin":
            print("Nice. Here's your key. Good Luck!")
        else:
            print("Try again.")

    elif answer == "no":
        print("You'll never see what's behind the door.")
    else:
        print("You need to pick something.")

else:
    print("Those are not the options. You die.")
