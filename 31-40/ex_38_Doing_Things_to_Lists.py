ten_things = "Apples Oranges Crows telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix")

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("Adding: ", next_one)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now.")

print("there we go: ", stuff)

print("let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff)) # what cool!
print("#".join(stuff[3:5]))
