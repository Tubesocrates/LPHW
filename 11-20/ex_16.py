 #List of commpands.
#• close – Closes the file. Like File->Save.. in your editor.
#• read – Reads the contents of the file. You can assign the result to a variable.
#• readline – Reads just one line of a text file.
#• truncate – Empties the file. Watch out if you care about the file.
#• write('stuff') – Writes “stuff” to the file.
#• seek(0) – Move the read/write location to the beginning of the file.

#One way to remember what each of these does is to think of a vinyl record,
#cassette tape, VHS tape, DVD, or CD player. In the early days of computers
#data was stored on each of these kinds of media, so many of the file
#operations still resemble a storage system that is linear. Tape and DVD drives
#need to “seek” a specific spot, and then you can read or write at that spot.
#Today we have operating systems and storage media that blur the lines
#between random access memory and disk drives, but we still use the older
#idea of a linear tape with a read/write head that must be moved.

#For now, these are the important commands you need to know. Some of them
#take parameters, but we do not really care about that. You only need to
#remember that write takes a parameter of a string you want to write to the
#file.

#Let’s use some of this to make a simple little text editor:

from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you dont want that, hit CTRL-C (^C) .")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# 'w' stands for writing permission for the opened file, you are calling it with the purpose
# or writing to it
target = open(filename, "w")


print("Truncating the file. Goodbye!")
#truncate empties the file
target.truncate()

print("Now I'm going to ask you for three lines.")
textlist = []
line1 = input("line 1: ")
textlist.append(line1)
line2 = input("line 2: ")
textlist.append(line2)
line3 = input("line 3: ")
textlist.append(line3)


print("I'm going to write these to the file.")
#below writes the three lines to our file
#before study drill 3
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#after study drill 3 this adds more lines
print("Lets double those lines.")
#old write COde, adds unnecessary strings
#target.write('%r\n%r\n%r\n' % (line1, line2, line3))

#new write code
for line in textlist:
  # write line to output file
  target.write(line)
  target.write("\n")
target.close()
#study drill number 2
# i had to close and then open the file to properly read the file. interesting

r_target = open(filename)
read = (r_target.read())


print(f"This is the newly formatted {filename}.")
print(read)
r_target.close()

#r_target2 = open(filename)
#filepath = 'text.py'
with open(filename) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line))#.strip()))
       line = fp.readline()
       cnt += 1
#read2 = (r_target2.readline(2))
#print("Line 2 is:", read2)

print("And finally, we close it.")
#this closes the in-use file
target.close()
