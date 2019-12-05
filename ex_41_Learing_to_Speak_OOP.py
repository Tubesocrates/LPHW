import random
from urllib.request import urlopen
import sys
a = """
In this exercise I’m going to teach you how to speak “object oriented.” What
I’ll do is give you a small set of words with definitions you need to know.
Then I’ll give you a set of sentences with holes in them that you’ll have to
understand. Finally, I’m going to give you a large set of exercises that you
have to complete to make these sentences solid in your vocabulary
"""
print(a)

definitions = {
	"class": "Tell Python to make a new type of thing",
	"object" : "Two meanings: the most basic type of thing, any instance of something",
	"instance" : "What you get when you tell python to create a class",
	"def" : "How you define a function inside of a class",
	"self" : "Inside the functions in a class, self is a var for the instance/obj being accessed.",
	"inheritance" : "The concept that one class can inherit traits from another class, like lineage",
	"composition" : "The concept that a class can be compased of other classes as parts, like a car has wheels",
	"attribute" : "A porpoerty classed have that are from coposition and are usually variables",
	"is-a" : "A phrase to say that someting inherits from another, as in a 'salmon' is a 'fish'",
	"has-a" : "A phrase to say that somehting is composed of other things or has a trait, 'a salmon has a mouth'"
}

print(definitions)


WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :"class %%% has-a __init__ that takes self and *** params.",
	"class %%%(object):\n\tdef ***(self, @@@)":"class %%% has-a function *** that takes self and @@@ params.",
	"*** = %%%()":"Set *** to an instance of class %%%.",
	"***.***(@@@)":"From *** get the *** function, call it with params self, @@@.",
	"***.*** = '***'":"From *** get the *** attribute and set it to '***'."
}
g = {
	"class %%%(%%%):": "Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" : "class %%% has-a __init__ that takes self and *** params.",
	"class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function *** that takes self and @@@ params.",
	"*** = %%%()":"Set *** to an instance of class %%%.",
	"***.***(@@@)":"From *** get the *** function, call it with params self, @@@.",
	"***.*** = '***'":"From *** get the *** attribute and set it to '***'."
}
# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', ' .join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)

	# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
	# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

			results.append(result)
	return results


# keep going until they hit CTRL-D
try:
	while True:
		snippets = list(PHRASES.keys())
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print(question)

			input("> ")
			print(f"ANSWER: {answer}\n\n")
except EOFError:
	print("\nBye")
