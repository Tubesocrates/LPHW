def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(" ")
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prins the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
#-----------------------------------------------------------------------------------
# Your output should look like mine, and after the > character (called the
# prompt) you can type Python code in, and it will run immediately. Using this
# I want you to type each of these lines of Python code into python3.6 and see
# what it does:
#-----------------------------------------------------------------------------------
# 1 import ex25
# 2 sentence = "All good things come to those who wait."
# 3 words = ex25.break_words(sentence)
# 4 words
# 5 sorted_words = ex25.sort_words(words)
# 6 sorted_words
# 7 ex25.print_first_word(words)
# 8 ex25.print_last_word(words)
# 9 words
# 10 ex25.print_first_word(sorted_words)
# 11 ex25.print_last_word(sorted_words)
# 12 sorted_words
# 13 sorted_words = ex25.sort_sentence(sentence)
# 14 sorted_words
# 15 ex25.print_first_and_last(sentence)
# 16 ex25.print_first_and_last_sorted(sentence)
#-----------------------------------------------------------------------------------
# Here’s what it looks like when I work with the ex25.py module in
# python3.6:
# Exercise 25 Python Session
# Python 3.6.0 (default, Feb 2 2017, 12:48:29)
# [GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ex25
# >>> sentence = "All good things come to those who wait."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
# >>> words
# ['good', 'things', 'come', 'to', 'those', 'who']
# >>> ex25.print_first_word(sorted_words)
# All
# >>> ex25.print_last_word(sorted_words)
# who
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)
# All
# wait.
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who
