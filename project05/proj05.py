##################################################################
#  CSE 231 Project 5
#  Ask the user for the file
#
#       Calculate the change between two consecutive years in percent
#       Print the largest change for each continent
#       Print the continent with the largest change
#
####################################################################


# Asks the user for the file, opens it and returns it as file
def open_file():
    a = 1
    # While loop is true until a real file is inputted
    while a == 1:
        try:
            file = open(input("Enter a file name:"))
            break
        except IOError:
            print("Error. Please try again.")
            a == 1
    return file


# Prints the header of the output
def print_headers():
    print("      Maximum Population Change by Continent\n")
    print("{:26s}{:>9s}{:>10s}".format("Continent", "Years", "Delta"))


# Calculates the changes between two consecutive years
def calc_delta(line, col):
    #Starts the string at index of 15 to slice of the name
    continent = line[15:]
    #The index start is based on column
    start = 6*(col-1)
    #First value
    first = int(continent[start:start+6])
    #Second value
    second = int(continent[start+6:start+12])
    #Delta is calculated based on the first and second values
    delta = (second-first)/first
    #Returns the delta
    return delta

# Prints of the continent, year, delta change in the specified format
def format_display_line(continent, year, delta):
    # Turns year into int
    year = int(year)
    # Multiples delta by 100 and rounds it
    delta = round(float(delta) * 100)
    # Prints the continent, years, and delta as a percent
    formatted_string = "{:<26s}{:4d}-{:<5d}{:8d}%".format(continent, year - 50, year, delta)
    return formatted_string


def main():
    # File is equal to the inputted file in open_file function
    file = open_file()
    # Prints the header
    print_headers()

    #Initializes max_of_max to 0
    max_of_max = 0

    #Enumerates lines in the file
    for i,line in enumerate(file):

        #If the line number is more than or equal to 1, it runs the code
        if i>=1:
            #For every line in the file it calculates the change through calc_delta()
            for line in file:
                #Continent isolates the name from the beginning of the string
                continent = line[:15].strip()
                min = -1

                #For loop loops through every column of the line
                for col in range(1,7):
                    #change is initialized to the calc_delta function
                    change = calc_delta(line, col)
                    #If the statement finds the largest delta change
                    if change >= min:
                        min = change
                        year = 1750 + (50 * col)
                #Prints of the statemnet
                print(format_display_line(continent, year, min))

                #Finds the max delta change in the all the max delta changes and prints it out
                if min > max_of_max:
                    max_of_max = min
                    max_of_max_year = year
                    max_of_max_continent = continent

            print("\nMaximum of all continents:")
            print(format_display_line(max_of_max_continent,max_of_max_year, max_of_max))

if __name__ == "__main__":
    main()
