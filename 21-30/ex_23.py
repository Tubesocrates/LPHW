# Exercise 23. Strings, Bytes, and Character Encodings
#------------------------------------------------------------
#           Run in powershell ISE
#------------------------------------------------------------
# To do this exercise you’ll need to download a text file that I’ve written
# named languages.txt This file was created with a list of human languages
# to demonstrate a few interesting concepts:
# 1. How modern computers store human languages for display and processing
# and how Python 3 calls this strings.
# 2. How you must “encode” and “decode” Python’s strings into a type called
# bytes.
# 3. How to handle errors in your string and byte handling.
# 4. How to read code and find out what it means even if you’ve never seen it
# before.
# In addition to that you’ll also get a brief glimpse of the Python 3 ifstatement
# and lists for processing a list of things. You don’t have to
# master this code or understand these concepts right away. You’ll get plenty of
# practice in later exercises. For now your job is to get a taste of the future and
# learn the four topics in the preceding list.
# Warning!
# This exercise is hard! There’s a lot of information in it that you need to
# understand, and it’s information that goes deep into computers. This exercise
# is complex because Python’s strings are complex and difficult to use. I
# recommend you take this exercise painfully slow. Write down every word
# you don’t understand, and look it up or research it. Take a paragraph at a time
# if you must. You can continue with other exercises while you study this one,
# so don’t get stuck here. Just chip away at it for as long as it takes.
# Initial Research
# I’m going to teach you how to research a piece of code to expose its secrets.
# You’ll need the languages.txt file for this code to work, so make sure you
# download it first. The languages.txt file simply

import sys
script, encoding, error = sys.argv
#this will be called at the end of this script
def main(language_file, encoding, errors):
    # this reads one line from the languages file it is given
    line = language_file.readline()
    #if line has anything in it, if it does not itll skip 41-42
    if line:
        #calls the function defined below
        print_line(line, encoding, errors)
        # we call main inside of itself, but the if loops stops ir from running forever
        return main(language_file, encoding, errors)
# this was the function called.
def print_line(line, encoding, errors):
    # this gets rid of the \n on the end of the line string
    next_lang = line.strip()
    # here we encode the language into raw bytes
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # now we adre decoding bytes
    # DBES = Decode Bytesm, Encode Strings

    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)
# we are done defining functions so we open the languaes.txt file

languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)
