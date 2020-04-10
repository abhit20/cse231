##################################################################
#  CSE 231 Project 7
#  Asks the user for the file to open and parse
#
#       Finds the states, count of native, naturalized, and non-citizens in the 2016
#       Calculates the ratio of naturalized to total residents and ratio of non-citizens to total residents
#       Finds the total counts from all the states for 2016 use calc_data
#       Finds the total count of total populations in year 2000
#       Print all the counts, ratios, and totals and plots it if the user wants to
####################################################################
import pylab  # needed for plotting

STATUS = ['Approved', 'Denied', 'Settled']

# Asks the user for the file, opens it and returns it as file
def open_file():
    a = True
    file = input("Please enter a file name: ")
    # While loop is true until a real file is inputted
    while a == True:
        try:
            file1 = open(file,'r')
            a=False
        except:
            file=input("File not found. Please enter a valid file name: ")

    return file1

#Reads the file inputted by the user
def read_file(fp):
    #Reads the first line
    header = fp.readline()
    # Creates a list of the header
    header_lst = header.split(",")
    #list to store the tuples
    data = []
    # Loops through the line in the file
    for i, line in enumerate(fp):

        # Line_list creates a list of the line
        line_lst = line.strip().split(",")

        #Gets Date Received (column 1) and .
        column1 = line_lst[1]
        #Gets Airport Name (column 4)
        column4 = line_lst[4]
        #Gets Airport Claim Amount (column 9) and replaces dollar sign and semicolon
        column9 = line_lst[9]
        column9r = column9.replace("$", "")
        column9r = column9r.replace(";", "")
        #Gets Status (column 10)
        column10 = line_lst[10]
        #Gets Close Amount (column 11)
        column11 = line_lst[11]
        column11r = column11.replace("$", "")
        column11r = column11r.replace(";", "")
        #If the the following columns is empty it ignores that row
        if column1=="" or column4==""or column9r == "" or column11r == "":
            pass
        else:
            #If the year is between 2002 and 2009 inclusive, the following code runs
            if column1[-2:] == '02' or column1[-2:] == '03' or column1[-2:] == '04' or column1[-2:] == '05' or column1[-2:] == '06' or column1[-2:] == '07' or column1[-2:] == '08' or column1[-2:] == '09':
                data.append((column1, column4, float(column9r), column10, float(column11r)))
    #Returns the tuple of the following values
    return(data)

#Processes the data after the file is read
def process(data):
    #Initializes variables
    max_claim=0.0
    n=0
    o=0
    total_claim=0
    #Initializes the arrays
    total_cases = [0,0,0,0,0,0,0,0,0,0]
    settled = [0,0,0,0,0,0,0,0,0,0]
    denied = [0,0,0,0,0,0,0,0,0,0]
    #Loops through every tuple in the data list
    for tup in data:
        #If status is accepted, denied, settled then the following code runs
        if tup[3] in STATUS:
            # n keeps the total number of tuples and increments total count in the total_cases
            n+=1
            total_cases[int(tup[0][-1])] +=1
            #If status is settled or approved, calculates average claim amount
            #  and increments settled list by one for every year
            if tup[3] == "Settled" or tup[3]=="Approved":
                settled[int(tup[0][-1])] +=1
                total_claim += float(tup[4])
                #If the value is not 0 then the o is not incremented by 1
                if tup[4] != 0:
                    o+=1
            #Average_total_claim is total_claim divided by count of values
            average_total_claim = total_claim / o
            #If status is denied increments denied year by one
            if tup[3] == "Denied":
                denied[int(tup[0][-1])] +=1
                #Finds the max claim amount and max claim airport
            if float(tup[2]) > max_claim:
                max_claim = float(tup[2])
                max_claim_airport = tup[1]
    #Pops the first two elements
    total_cases = total_cases[2:]
    settled= settled[2:]
    denied = denied[2:]
    #Returns a tuple of the following
    return ((total_cases,settled,denied,n,average_total_claim,max_claim,max_claim_airport))

#Displays the data
def display_data(tup):

    print("TSA Claims Data: 2002 - 2009 \n")
    print("N = {:,d}\n".format(tup[3]))
    print("{:<8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format(" ", '2002', '2003', '2004', '2005', '2006',
                                                                          '2007', '2008', '2009'))
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}".format("Total", tup[0][0], tup[0][1], tup[0][2], tup[0][3], tup[0][4],
                                                                          tup[0][5], tup[0][6], tup[0][7]))
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}".format("Settled", tup[1][0], tup[1][1], tup[1][2], tup[1][3], tup[1][4],
                                                                          tup[1][5], tup[1][6], tup[1][7]))
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}".format("Denied", tup[2][0], tup[2][1], tup[2][2], tup[2][3], tup[2][4],
                                                                          tup[2][5], tup[2][6], tup[2][7]))
    print("\nAverage settlement: ${:,.2f}".format(tup[4]))
    print("The maximum claim was ${:,.2f} at {} Airport\n".format(tup[5],tup[6]))

def plot_data(accepted_data, settled_data, denied_data):
    '''Plot the three lists as bar graphs.'''

    X = pylab.arange(8)  # create 8 items to hold the data for graphing
    # assign each list's values to the 8 items to be graphed, include a color and a label
    pylab.bar(X, accepted_data, color='b', width=0.25, label="total")
    pylab.bar(X + 0.25, settled_data, color='g', width=0.25, label="settled")
    pylab.bar(X + 0.50, denied_data, color='r', width=0.25, label="denied")

    # label the y axis
    pylab.ylabel('Number of cases')
    # label each bar of the x axis
    pylab.xticks(X + 0.25 / 2, ("2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009"))
    # create a legend
    pylab.legend(loc='best')
    # draw the plot
    pylab.show()
    # optionally save the plot to a file; file extension determines file type
    # pylab.savefig("plot.png")

def main():
    #Runs the open_file() to input file from user
    fp = open_file()
    #Reads the file in read_file()
    data = read_file(fp)
    #Parses the data in process()
    tup = process(data)
    #Displays the data in display_data()
    display_data(tup)
    # Plots the data if the user inputs yes
    if input("Plot data (yes/no): ").lower() == "yes":
        plot_data(tup[0], tup[1], tup[2])

if __name__ == "__main__":
    main()