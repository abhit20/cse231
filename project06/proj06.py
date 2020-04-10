##################################################################
#  CSE 231 Project 6
#  Asks the user for the file to open and parse
#
#       Finds the states, count of native, naturalized, and non-citizens in the 2016
#       Calculates the ratio of naturalized to total residents and ratio of non-citizens to total residents
#       Finds the total counts from all the states for 2016 use calc_data
#       Finds the total count of total populations in year 2000
#       Print all the counts, ratios, and totals and plots it if the user wants to
####################################################################

import pylab  # for plotting
import operator  # useful for sorting

# Asks the user for the file, opens it and returns it as file
def open_file():
    a = 1
    # While loop is true until a real file is inputted
    while a == 1:
        try:
            file = open(input("Enter a file name: "))
            break
        except IOError:
            print("Error. Please try again.")
            a == 1
    return file

#Finds the index of the string
def find_index(header_lst, s):
    # Finds the index of the string s in the header_list
    try:
        index = header_lst.index(s)
        return index
    #If value error, returns none
    except ValueError:
        return None

#Reads the 2016 file
def read_2016_file(fp):
    #Reads the header line in the file
    header = fp.readline()

    #Creates a list of the header
    header_lst = header.split(",")

    #Initializes list to be appended
    state_values_2016=[]

    #Loops through the line in the file
    for i,line in enumerate(fp):
        #Skips line 1
        if i == 0:
            continue
        else:
            #Line_list creates a list of the line
            line_lst = line.strip().split(",")
            #State is equal to the name of the state
            state=line_lst[2].strip()
            #Native_index is equal to the index of the native value
            native_index = find_index(header_lst, "EST_VC197")
            # Naturalizes_index is equal to the index of the naturalized value
            naturalized_index = find_index(header_lst, "EST_VC201")
            # Non_citizens_index is equal to the index of the non_citizens value
            non_citizens_index = find_index(header_lst, "EST_VC211")
            #Uses the native_index to find the value
            native_value = int(line_lst[native_index])

            # Uses the natualized_index to find the value
            naturalized_value = int(line_lst[naturalized_index])

            # Uses the non_citizens_index to find the value
            non_citizens_value = int(line_lst[non_citizens_index])

            #Total_citizens is the sum of native, naturalized and non citizens
            total_citizens = native_value + naturalized_value + non_citizens_value
            #Ratio_naturalized is naturalized_value divided by total_citizens
            ratio_naturalized = naturalized_value/total_citizens

            # Ratio_non_citizens is non_citizens_value divided by total_citizens
            ratio_non_citizens = non_citizens_value/total_citizens

            #Appens values to the state_values list
            state_values_2016.append((state,native_value,naturalized_value,ratio_naturalized,non_citizens_value,ratio_non_citizens))

    #Returns the list state_values_2016
    return(state_values_2016)

#Reads the 2000 file
def read_2000_file(fp2):
    # Reads the header line in the file
    header = fp2.readline()

    # Creates a list of the header
    header_lst = header.split(",")

    # Loops through the line in the file
    for i, line in enumerate(fp2):
        # Skips line 1
        if i == 0:
            continue
        else:
            # Line_list creates a list of the line
            line_lst = line.strip().split(",")
            # State is equal to the name of the state
            state = line_lst[2].strip()
            # Native_index is equal to the index of the native value
            native_index = find_index(header_lst, "HC01_VC03")
            # Naturalizes_index is equal to the index of the naturalized value
            naturalized_index = find_index(header_lst, "HC01_VC05")
            # Non_citizens_index is equal to the index of the non_citizens value
            non_citizens_index = find_index(header_lst, "HC01_VC06")
            #Total_citizens_index is equal to the index of the total_citizens value
            total_citizens_index = find_index(header_lst, "HC01_VC02")
            # Uses the native_index to find the value
            native_value = int(line_lst[native_index])

            # Uses the natualized_index to find the value
            naturalized_value = int(line_lst[naturalized_index])

            # Uses the non_citizens_index to find the value
            non_citizens_value = int(line_lst[non_citizens_index])

            # Uses the total_citizens_index to find the value
            total_citizens_value = int(line_lst[total_citizens_index])

    #Returns the tuple of the following values
    return (total_citizens_value, native_value, naturalized_value, non_citizens_value)

#Calculates the total of all the counts
def calc_totals(data_sorted):
    #Initializes the variables to be added to
    total_native, total_naturalized,total_non_citizens = 0,0,0
    #For each state, each state states are added to the variables above
    for tup in data_sorted:
        total_native +=tup[1]
        total_naturalized +=tup[2]
        total_non_citizens +=tup[4]
    #Finds the total_residents of US
    total_residents = total_native+total_naturalized+total_non_citizens
    #Returns the values
    return(total_native, total_naturalized,total_non_citizens,total_residents)

#Makes list so it can be plotted
def make_lists_for_plot(native_2000, naturalized_2000, non_citizen_2000, native_2016, naturalized_2016,
                        non_citizen_2016):
    return([native_2000,native_2016],[naturalized_2000,naturalized_2016],[non_citizen_2000,non_citizen_2016])

#Plots the data
def plot_data(native_list, naturalized_list, non_citizen_list):
    '''Plot the three lists as bar graphs.'''

    X = pylab.arange(2)  # create 2 containers to hold the data for graphing
    # assign each list's values to the 3 items to be graphed, include a color and a label
    pylab.bar(X, native_list, color='b', width=0.25, label="native")
    pylab.bar(X + 0.25, naturalized_list, color='g', width=0.25, label="naturalized")
    pylab.bar(X + 0.50, non_citizen_list, color='r', width=0.25, label="non-citizen")

    pylab.title("US Population")
    # label the y axis
    pylab.ylabel('Population (hundred millions)')
    # label each bar of the x axis
    pylab.xticks(X + 0.25 / 2, ("2000", "2016"))
    # create a legend
    pylab.legend(loc='best')
    # draw the plot
    pylab.show()
    # optionally save the plot to a file; file extension determines file type
    # pylab.savefig("plot.png")


def main():
    #Runs open_file() teice to open 2016 and 2000 files
    fp = open_file()
    fp2 = open_file()
    #Sorts 2016 data in ascending order based on ratios on non-citizens to total
    data_sorted_2016 = read_2016_file(fp)
    data_sorted_2016.sort(key=operator.itemgetter(5))
    #Calculates the totals for the 2016 counts
    totals_2016 = calc_totals(data_sorted_2016)

    #Prints the headers
    print("\n                               2016 Population: Native, Naturalized, Non-Citizen\n")

    print("{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}".format("State", "Native", "Naturalized", "Percent Naturalized",
                                                              "Non-Citizen", "Percent Non-Citizen"))

    #Prints the data from 2016 for each state
    for tup in data_sorted_2016:
        print("{:<20s}{:15,d}{:17,d}{:>21.1f}%{:16,d}{:>21.1f}%".format(tup[0],tup[1],tup[2],tup[3]*100,tup[4],tup[5]*100))
    print("-"*112)

    #Prints the totals from 2016 and 200 respectively
    print("{:<20s}{:15,d}{:17,d}{:>21.1f}%{:16,d}{:>21.1f}%".format("Total 2016",totals_2016[0],totals_2016[1],(totals_2016[1]/totals_2016[3])*100,totals_2016[2],(totals_2016[2]/totals_2016[3])*100))

    totals_2000 = read_2000_file(fp2)
    print("{:<20s}{:15,d}{:17,d}{:>21.1f}%{:16,d}{:>21.1f}%".format("Total 2000", totals_2000[1], totals_2000[2],
                                                                    (totals_2000[2] / totals_2000[0]) * 100,
                                                                    totals_2000[3],
                                                                    (totals_2000[3] / totals_2000[0]) * 100))
    #Plots the data if the user inputs yes
    if input("Do you want to plot? ").lower() == "yes":
        make_lists = make_lists_for_plot(totals_2000[1], totals_2000[2], totals_2000[3], totals_2016[0], totals_2016[1],
                            totals_2016[2])
        plot_data(make_lists[0],make_lists[1],make_lists[2])


if __name__ == "__main__":
    main()