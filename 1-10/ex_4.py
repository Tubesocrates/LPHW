#-----------------------------------------
#-----------------------------------------
#           VARIABLES
#-----------------------------------------
#-----------------------------------------
#Defining how many cars there are
#spaces are great practice
cars = 100
#below is a float, and the amount of seats in each car
space_in_a_car = 4.0
#defining how many drivers there are
drivers = 30
#defining how many passengers there are
passengers = 90
#this finds the amount of cars not driven
cars_not_driven = cars - drivers
#the total amount of cars driven is obviously equal to the cars_driven
cars_driven = drivers
# the capacity available to carpool, the amount of cars used*the space in
# a car
carpool_capacity = cars_driven * space_in_a_car
#finding the average passengers per car, by taking the passengers / cars_driven
average_passengers_per_car = passengers / cars_driven
#-----------------------------------------
#-----------------------------------------
#           CODE
#-----------------------------------------
#-----------------------------------------
#here we are making a statement about how many cars are available
# we can use "cars" to put the number within this print
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
