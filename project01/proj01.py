#
# CSE 231 Project 1
#
#   Ask for an input in rods
#   Converts the rods into meters, feet, miles, furlongs
#   Prints each unit conversion individually
#   Calcuates the minutes to walk to walk the inputted rods and prints it
#   All the units are rounded to three places
#


#Asks the user for input rods and turns it into float for further calculations.
input_rods = float(input('Input rods: '))

#Prints the user input and a new line
print("You input ",input_rods," rods.\n")

#Prints the word "Conversions"
print("Conversions")

# Converts rods into meters
convert_to_meters = input_rods * 5.0292
#Prints meters
print("Meters: ",round(convert_to_meters,3))

# Converts meters into feet
convert_to_feet = convert_to_meters /0.3048
#Prints feet
print("Feet: ", round(convert_to_feet,3))

# Converts meters into miles
convert_to_miles = convert_to_meters / 1609.34
#Prints miles
print("Miles: ", round(convert_to_miles,3))

# Converts rods into furlongs
convert_to_furlongs = input_rods / 40
#Prints furlongs
print("Furlongs: ", round(convert_to_furlongs,3))

# Calculates the number of minutes it takes to walk the inputted rods
minutes_to_walk = float(input_rods) / 1609.34 * 5.0292 / 3.1 * 60
#Prints minutes to walk the inputted rods
print("Minutes to walk ",input_rods,"rods:",round(minutes_to_walk, 3))