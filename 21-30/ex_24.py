print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely worls
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t where there is none.
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

#remebmer that this is anpother way to format a string

print("With a starting point of {}".format(start_point))
#this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(beans, jars, crates))

start_point = start_point/10

#it's just like with and f"" string
print("We can also do it this way:")
formula = secret_formula(start_point)

#this is an easy way to apply a list to a format string
print("We'd have %d beans, %d jars, and %d crates." % formula)
