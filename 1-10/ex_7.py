print("Mary had a little lamb.")
#this prints the following statement formatting snow into the {}
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
#this prints 10 periods in a row
print("."*10) #what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#below we print all the ends together by adding them
# watch end = ' ' at the end. tey removing it and to see what happens
# if I remove it it doesnt continue the word

# it prints
#->   Cheese
#->   Burger

# instead of
#->   Chese Burger

print(end1 + end2 + end3 + end4 + end5 + end6, end = ' @ ')
# print(end1 + end2 + end3 + end4 + end5 + end6)#, #end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
