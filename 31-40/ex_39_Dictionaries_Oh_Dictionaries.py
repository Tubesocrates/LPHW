#----------------------
#		Lists
#----------------------
things = ['a', 'b', 'c', 'd']
print(things)
print("things[1] =", things[1])

things[1] = 'z'
print("Changing the second entry to z")
print(things)
print("things[1] =", things[1])
#----------------------
#		Dicts
#----------------------
stuff = {'name': "Jash", 'age': "26", 'height': 5*12+9}

print(stuff['name'])

print(stuff['age'])

print(stuff['height'])

print("Adding and key and value, city and saratoga")
stuff['city'] = "SS"
print("stuff['city'] =", stuff['city'])

print("\n")
print("We dont have to use strings")

stuff[1] = "wow"
stuff[2] = "neato"
print("New stuff = ", stuff[1] + "," + stuff[2])

print("\n")
print("We can delete stuff too")
del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)

print("\n")
print("Lets create a mapping of state to abbreviation")

states = {
	"Oregon":"OR",
	"Florida":"FL",
	"California":"CA",
	"New York": "NY",
	"Michigan": "MI"
}
print("Lets create a mapping of states with cities in them")
cities = {
	"CA":"San Francisco",
	"MI": "Detroit",
	"FL":"Jacksonville"
}

print("Let's add some more cities")
cities['NY'] = 'New York'
cities['OR'] = "Portland"
print("\n")

print('-' * 10)
print("Some cities")
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-' * 10)
print("some states")
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
print("\n")

print('-' * 10)
print("Lets use the state then the cities dict")
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

print('-' * 10)
print("Every States abbreviation")
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}.")

print('-' * 10)
print("Every City in State")
for abbrev, city  in list(cities.items()):
	print(f"{abbrev} has the city {city}.")

print("\n")

print('-' * 10)
print("Now lets do both at the same time.")
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has the city {cities[abbrev]}.")

print('-' * 10)
print("Get an abbreviation that may not be there")
state = states.get("Texas")

if not state:
	print("Sorry that state doesnt exist.")

print('-' * 10)
print("Get a city with a default value")
city = cities.get("TX", "Does not exist")
print(f"The city for the state 'TX' is: {city}")
