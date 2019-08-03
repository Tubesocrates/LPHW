#-----------------------------------------
#-----------------------------------------
#           VARIABLES
#-----------------------------------------
#-----------------------------------------

my_name = 'Josh W. Johnson'
my_age = 25 #not a lie
my_height = 69 #inches
my_weight = 190 #lbs
my_eyes = 'Brown'
my_shoes = 'Grey'
my_hair = 'Brown'
my_height_cm = my_height*2.4
my_weight_kg = round(my_weight/2.205)

#-----------------------------------------
#-----------------------------------------
#           CODE
#-----------------------------------------
#-----------------------------------------

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"So he's {my_height_cm} centimeters tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"So he's {my_weight_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His shoes are usually {my_shoes} depending on the weather.")

#this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
