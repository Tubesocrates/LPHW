import glob
print("Here's a list of files:")
m = []
def filebrowser():
	i = 1
	for f in glob.glob("*_[0-9][0-9]*.py"):
		print(i, f)
		m.append(f)
		i += 1
	# return m


def choose():
	BooleanProperty = False
	while BooleanProperty == False:
		print("Choose a file by typing in the corresponding number:")
		choice = int(input(">")) - 1
		print(m[choice-1])
		print("\n")
		if choice <= len(m):
			print("Opening.....")

			print(m[choice])
			exec(open(m[choice]).read())
			BooleanProperty = True
		else:
			print("Choose one of the numbers please.")
x = filebrowser()
print(x)
choose()
