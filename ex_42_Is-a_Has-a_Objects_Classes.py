a = """
An important concept that you have to understand is the difference between a
class and an object. The problem is, there is no real “difference” between a
class and an object. They are actually the same thing at different points in
time. I will demonstrate by a Zen koan:
What i s the difference between a f i s h and a salmon?
Did that question sort of confuse you? Really sit down and think about it for a
minute. I mean, a fish and a salmon are different but, wait, they are the same
thing, right? A salmon is a kind of fish, so I mean it’s not different. But at the
same time, a salmon is a particular type of fish so it’s actually different from
all other fish. That’s what makes it a salmon and not a halibut. So a salmon
and a fish are the same but different. Weird.
This question is confusing because most people do not think about real things
this way, but they intuitively understand them. You do not need to think
about the difference between a fish and a salmon because you know how they
are related. You know a salmon is a kind of fish and that there are other kinds
of fish without having to understand that.
Let’s take it one step further. Let’s say you have a bucket full of three salmon
and because you are a nice person, you have decided to name them Frank,
Joe, and Mary. Now, think about this question:
What i s the difference between Mary and a salmon?
Again this is a weird question, but it’s a bit easier than the fish versus salmon
question. You know that Mary is a salmon, so she’s not really different. She’s
just a specific “instance” of a salmon. Joe and Frank are also instances of
salmon. What do I mean when I say instance? I mean they were created from
some other salmon and now represent a real thing that has salmon-like
attributes.
Now for the mind-bending idea: Fish is a class, and Salmon is a class, and
Mary is an object. Think about that for a second. Let’s break it down slowly
and see if you get it.
A fish is a class, meaning it’s not a real thing, but rather a word we attach to
instances of things with similar attributes. Got fins? Got gills? Lives in
water? Alright it’s probably a fish.
Someone with a Ph.D. then comes along and says, “No, my young friend, this
fish is actually Salmo salar, affectionately known as a salmon.” This
professor has just clarified the fish further, and made a new class called
“Salmon” that has more specific attributes. Longer nose, reddish flesh, big,
lives in the ocean or fresh water, tasty? Probably a salmon.
Finally, a cook comes along and tells the Ph.D., “No, you see this Salmon
right here, I’ll call her Mary, and I’m going to make a tasty fillet out of her
with a nice sauce.” Now you have this instance of a salmon (which also is an
instance of a fish) named Mary turned into something real that is filling your
belly. It has become an object.
There you have it: Mary is a kind of salmon that is a kind of fish—object is a
class is a class.
..............................
How This Looks in Code
..............................
This is a weird concept, but to be very honest you only have to worry about it
when you make new classes and when you use a class. I will show you two
tricks to help you figure out whether something is a class or an object.
First, you need to learn two catch phrases “is-a” and “has-a.” You use the
phrase is-a when you talk about objects and classes being related to each
other by a class relationship. You use has-a when you talk about objects and
classes that are related only because they reference each other.
Now, go through this piece of code and replace each ##?? comment with a
comment that says whether the next line represents an is-a or a has-a
relationship and what that relationship is. In the beginning of the code, I’ve
laid out a few examples, so you just have to write the remaining ones.
Remember, is-a is the relationship between fish and salmon, while has-a is
the relationship between salmon and gills.
"""
print(a)
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
# dog is-a animal
class Dog(Animal):
	def __init__(self, name):
		## dog has a name
		self.name = name
# cat is-a animal
class Cat(Animal):
	def __init__(self, name):
		## cat has a name
		self.name = name
## person is an object
class Person(object):
	def __init__(self, name):
		## person has a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None
## employee is a person
class Employee(Person):
	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		# super allows for refering to the superclass implicitly, so
		# super(Employee, self).__init__(name)
		# this is how you write this in python 3
		super().__init__(name)
		## employee has a salary,
		self.salary = salary
## fish is an object
class Fish(object):
	pass
## salmon is a fish
class Salmon(Fish):
	pass
## halibut is a fish
class Halibut(Fish):
	pass
## rover is-a Dog
rover = Dog("Rover")
print(rover)
## satan is a cat
satan = Cat("Satan")
print(satan)
## mary is a person
mary = Person("Mary")
print(mary)
## has a
mary.pet = satan
print(mary.pet)
## is a that has a salary
frank = Employee("Frank", 120000)
print(frank)
## ??
frank.pet = rover
print(frank.pet)
## ??
flipper = Fish()
## ??
crouse = Salmon()
## ??
harry = Halibut()
