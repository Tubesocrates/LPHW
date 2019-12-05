# 1. Rules for If-Statements
    #I do these to the last code
            # 1. Every if-statement must have an else.
            # 2. If this else should never run because it doesn’t make sense, then you must
            #    use a die function in the else that prints out an error message and dies, just
            #    like we did in the last exercise. This will find many errors.
            # 3. Never nest if-statements more than two deep and always try to do them
            #    one deep.
            # 4. Treat if-statements like paragraphs, where each if-elif-else grouping
            #    is like a set of sentences. Put blank lines before and after.
            # 5. Your Boolean tests should be simple. If they are complex, move their
            #    calculations to variables earlier in your function and use a good name for the
            #    variable.
# If you follow these simple rules, you will start writing better code than most
# programmers. Go back to the last exercise and see if I followed all of these
# rules. If not, fix my mistakes.

# 2. Rules for Loops
            # 1. Use a while-loop only to loop forever, and that means probably never.
            #    This only applies to Python; other languages are different.
            # 2. Use a for-loop for all other kinds of looping, especially if there is a fixed
            #    or limited number of things to loop over.

from sys import exit
#defines the gold room
# tests #1
def gold_room():
        print("This room is full of gold. How much do you take?")
        # i can make this more elegant
            # making it simpiler with int in the beginning
        choice = int(input("> "))
        if int(input('> ')):
            how_much = int(choice)
            # nested one deep rule 3
            if how_much < 50:
                print("Nice, your're not greedy, you win!")
                exit(0)
            #cathcall
            # rule 2 else will run
            else:
                dead("You greedy bastard!")
        #cathcall
        else:
            dead("Man, learn to type a number.")


# defines bear room
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    # we define bear moved as false at first, this is to ____
    bear_moved = False
    # this makes and infinite loop
    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face.")
        # this breaks out of the loop i think
        # if choice is taunt bear and true, then the bear will move
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        # if choice is taunt bear and false then the bear will chew your leg off
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        # once the bear is moved you can now open the door
        elif choice == "open door" and bear_moved:
            gold_room()
        # catchall
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        # restarts the game
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    # means a clean exit
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()

# Homework
        # Now write a game similar to the one that I created in the last exercise. It can
        # be any kind of game you want in the same flavor. Spend a week on it making
        # it as interesting as possible. For Study Drills, use lists, functions, and
        # modules (remember those from Exercise 13?) as much as possible, and find
        # as many new pieces of Python as you can to make the game work.
        
# Before you start coding you must draw a map for your game. Create the
# rooms, monsters, and traps that the player must go through on paper before
# you code.
# Once you have your map, try to code it up. If you find problems with the map
# then adjust it and make the code match.
# The best way to work on a piece of software is in small chunks like this:
# 1. On a sheet of paper or an index card, write a list of tasks you need to
# complete to finish the software. This is your to do list.
# 2. Pick the easiest thing you can do from your list.
# 3. Write out English comments in your source file as a guide for how you
# would accomplish this task in your code.
# 4. Write some of the code under the English comments.
# 5. Quickly run your script so see if that code worked.
# 6. Keep working in a cycle of writing some code, running it to test it, and
# fixing it until it works.
# 7. Cross this task off your list, then pick your next easiest task and repeat.
# This process will help you work on software in a methodical and consistent
# manner. As you work, update your list by removing tasks you don’t really
# need and adding ones you do.
