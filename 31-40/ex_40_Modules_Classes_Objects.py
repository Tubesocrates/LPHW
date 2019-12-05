import Mystuff
print("Modules Are Like Dictionaries")
x = """You know how a dictionary is created and used and that it is a way to map
one thing to another. That means if you have a dictionary with a key "apple"
and you want to get it then you do this:
"""
print(x)
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])
print('-' * 10)
y = """Keep this idea of "get X from Y" in your head, and now think about modules.
You've made a few so far, and you should know they are:
1. A Python file with some functions or variables in it ..
2. You import that file.
3. And you can access the functions or variables in that module with the .
(dot) operator.
Imagine I have a module that I decide to name mystuff.py and I put a
function in it called apple. Here's the module mystuff.py:
"""
print(y)
print('-' * 10)
Mystuff.apple()
print(Mystuff.tangerine)
print('-' * 10)
z = """Refer back to the dictionary, and you should start to see how this is similar to
using a dictionary, but the syntax is different. Let's compare:
"""
print(z)
print("Get the apple froom the dict")
mystuff['apple']
print("Get the apple from the module")
Mystuff.apple()
print('-' * 10)
a = """This means we have a very common pattern in Python:
1. Take a key=value style container.
2. Get something out of it by the key's name.
In the case of the dictionary, the key is a string and the syntax is [key]. In the
case of the module, the key is an identifier, and the syntax is .key. Other than
that they are nearly the same thing.
"""
print(a)



print("Classes are like modules")
b = """
You can think about a module as a specialized dictionary that can store
Python code so you can access it with the . operator. Python also has another
construct that serves a similar purpose called a class. A class is a way to take
a grouping of functions and data and place them inside a container so you can
access them with the . (dot) operator.
If I were to create a class just like the mystuff module, I'd do something like
this:
"""
print('-' * 10)
class my_stuff(object):
	def __init__(self):
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print("I am classy apples")

c = """That looks complicated compared to modules, and there is definitely a lot
going on by comparison, but you should be able to make out how this is like
a "mini-module" with MyStuff having an apple() function in it. What is
probably confusing is the __init__() function and use of self.tangerine
for setting the tangerine instance variable.
Here's why classes are used instead of modules: You can take this MyStuff
class and use it to craft many of them, millions at a time if you want, and
each one won't interfere with each other. When you import a module there is
only one for the entire program unless you do some monster hacks.
Before you can understand this though, you need to know what an "object" is
and how to work with MyStuff just like you do with the mystuff.py module.
"""
print('-' * 10)
print(c)

print("Objects are like import.")
d = """
If a class is like a "mini-module," then there has to be a concept similar to
import but for classes. That concept is called "instantiate", which is just a
fancy, obnoxious, overly smart way to say "create." When you instantiate a
class what you get is called an object.
You instantiate (create) a class by calling the class like it's a function, like
this:
"""
print('-' * 10)

thing = my_stuff()
thing.apple()
print(thing.tangerine)

print('-' * 10)
e = """
1 thing = MyStuff()
2 thing.apple()
3 print(thing.tangerine)
The first line is the "instantiate" operation, and it's a lot like calling a
function. However, Python coordinates a sequence of events for you behind
the scenes. I'll go through these steps using the preceding code for MyStuff:
1. Python looks for My_Stuff() and sees that it is a class you've defined.
2. Python crafts an empty object with all the functions you've specified in the
class using def.
3. Python then looks to see if you made a "magic" __init__ function, and if
you have it calls that function to initialize your newly created empty object.
4. In the MyStuff function __init__ I then get this extra variable self, which
is that empty object Python made for me, and I can set variables on it just like
you would with a module, dictionary, or other object.
5. In this case, I set self.tangerine to a song lyric and then I've initialized
this object.
6. Now Python can take this newly minted object and assign it to the thing
variable for me to work with.
That's the basics of how Python does this "mini-import" when you call a class
like a function. Remember that this is not giving you the class but instead is
using the class as a blueprint for building a copy of that type of thing.
Keep in mind that I'm giving you a slightly inaccurate idea of how these work
so that you can start to build up an understanding of classes based on what
you know about modules. The truth is, classes and objects suddenly diverge
from modules at this point. If I were being totally honest, I'd say something
more like this:
• Classes are like blueprints or definitions for creating new mini-modules.
• Instantiation is how you make one of these mini-modules and import it at
the same time. "Instantiate" just means to create an object from the class.
• The resulting created mini-module is called an object, and you then assign it
to a variable to work with it.
At this point objects behave differently from modules, and this should only
serve as a way for you to bridge over to understanding classes and objects.
"""
print(e)
print("I now have 3 ways of getting things from things")
print("dict style")
print(mystuff['apple'])

print("module style")
Mystuff.apple()
print(Mystuff.tangerine)

print('class style')
things = my_stuff()
things.apple()
print(things.tangerine)

print('-' * 10)
print('-' * 10)
print('-' * 10)
print('\n')

f = """
40.1.4 A First Class Example
You should start seeing the similarities in these three key=value container
types and probably have a bunch of questions. Hang on with the questions, as
the next exercise will hammer home your "object-oriented vocabulary." In
this exercise, I just want you to type in this code and get it working so that
you have some experience before moving on.
"""

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family", "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
