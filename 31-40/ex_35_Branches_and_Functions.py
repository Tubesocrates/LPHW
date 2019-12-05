from sys import exit
#defines the gold room
def gold_room():
        print("This room is full of gold. How much do you take?")
        # i can make this more elegant
        choice = input("> ")
        if "0" in choice or "1" in choice:
            how_much = int(choice)
        #cathcall
        else:
            dead("Man, learn to type a number.")

        if how_much < 50:
            print("Nice, your're not greedy, you win!")
            exit(0)
        #cathcall
        else:
            dead("You greedy bastard!")
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

# Study Drills
# 1. Draw a map of the game and how you flow through it.
    # no
# 2. Fix all of your mistakes, including spelling mistakes.
# did
# 3. Write comments for the functions you do not understand.
# 4. Add more to the game. What can you do to both simplify and expand it?
# 5. The gold_room has a weird way of getting you to type a number. What are
# all the bugs in this way of doing it? Can you make it better than what I’ve
# written? Look at how int() works for clues.
