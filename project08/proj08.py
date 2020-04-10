##################################################################
#  CSE 231 Project 8
#  Asks the user for the file to open and parse
#
#       Finds and creates a dictionary of gender,geographic_area,diabetes,population, and other properties
#       Uses that dictionary to find the total diabetes and total population in each country
#       Uses the initial dictionary to prepare data for plot
#       Displays a table of d
#       Creates bar and pie plots if the user says yes
####################################################################

import pylab
from operator import itemgetter   # optional, if you use itemgetter when sorting

REGIONS = {'MENA': 'Middle East and North Africa', 'EUR': 'Europe',
           'AFR': 'Africa', 'NAC': 'North America and Caribbean',
           'SACA': 'South and Central America',
           'WP': 'Western Pacific', 'SEA': 'South East Asia'}

#Opens file
def open_file():
    a = True
    file = input("Please enter a file name: ")
    # While loop is true until a real file is inputted
    while a==True:
        try:
            file1 = open(file, encoding="windows-1252")
            a=False
        except:
            file=input("File not found. Please enter a valid file name: ")

    return file1

# Creates dictionary of the countries and their data for each age group
def create_dictionary(fp):
    # Initializes a list of all the line in the file
    line_lst=[]

    # Loops through every line after skipping the fist two lines
    for i,line in enumerate(fp):

        # Skips the first two lines
        if i >= 1:
            # Strips and splits each line and adds it to the dict
            line=line.strip().split(',')
            line_lst+=[line]
        # Sorts the list based on the index 2
        line_lst= sorted(line_lst,key=itemgetter(2))
        #Initializes the dict
        dict = {}

        # For the each list in the line_lst the following code runs
        for list in line_lst:
            # Finds country at index 1
            country = list[1]
            # Finds region at index 2
            region = list[2]
            # Finds age_group at index 3
            age_group = list[3]
            # Finds gender at index 4
            gender = list[4]
            # Finds geographic_area at index 5
            geographic_area = list[5]
            # Finds diabetes at index 6
            diabetes = int(float(list[6]) * 1000)
            # Finds population at index 7
            population = int(float(list[7]) * 1000)

            #Creates a list
            list = []
            #Makes a tuple out of the list and appends to the the list above
            tup = [gender,geographic_area,diabetes,population]
            tup=tuple(tup)
            list.append(tup)
            # Creates a region dictionary out of regions
            if region not in dict:
                region_dict = dict[region] = {}
            # Creates a country_dict inside region_dict
            if country not in region_dict:
                country_dict = region_dict[country] = {}
                #Creates a age_group list inside country_dict
            if age_group not in country_dict:
                country_dict[age_group] = list
            else:
                country_dict[age_group].append(tup)

    #Retruns the final dict
    return dict


def get_country_total(data):
    # Creates a dictionary with the countries and the totals
    country_total = {}

    # Loops through the data with country and its dictionary
    for country,dict in data.items():
        # Initailizes total_diabetes and total_population variables
        total_diabetes = 0
        total_pop = 0
        # Loops through each list in the list
        for tup in dict.values():
            # Loops through each individual tuple in the list
            for vals in tup:
                # Adds the total diabetes population to the total_diabetes count
                total_diabetes += vals[2]
                # Adds the each population to the total_population count
                total_pop += vals[3]
        # Appends to the dictionary with country as key and tup of total_diabetes and total_population as values
        country_total[country] = (total_diabetes,total_pop)

    # Returns country_total
    return country_total

# Prints the table
def display_table(data, region):
    #Print
    print("     Diabetes Prevalence in {}".format(REGIONS[region.upper()]))
    print("{:<25s}{:>20s}{:>16s}\n".format("Country Name", "Diabetes Prevalence", "Population"))
    for a,b in data.items():
        print("{:<25s}{:>20,d}{:>16,d}".format(a, b[0], b[1]))

#Prepares data to be data
def prepare_plot(data):
    # Initializes plot dict
    plot = {}
    #For each value in the data, it loops
    for i in data:
        # For each value in the data[i], it does the following
        for j in data[i]:
            #If j is in plot
            if j in plot:
                # Male and female values are added to the plot dict
                plot[j]["MALE"] += data[i][j][1][2]
                plot[j]["FEMALE"] += data[i][j][0][2]
            else:
                plot[j] = {"MALE": data[i][j][1][2],"FEMALE": data[i][j][0][2]}

    #Returns plot
    return (plot)

#Plots data
def plot_data(plot_type, data, title):
    '''
        This function plots the data.
            1) Bar plot: Plots the diabetes prevalence of various age groups in
                         a specific region.
            2) Pie chart: Plots the diabetes prevalence by gender.

        Parameters:
            plot_type (string): Indicates what plotting function is used.
            data (dict): Contains the dibetes prevalence of all the contries
                         within a specific region.
            title (string): Plot title

        Returns:
            None

    '''

    plot_type = plot_type.upper()

    categories = data.keys()  # Have the list of age groups
    gender = ['FEMALE', 'MALE']  # List of the genders used in this dataset

    if plot_type == 'BAR':

        # List of population with diabetes per age group and gender
        female = [data[x][gender[0]] for x in categories]
        male = [data[x][gender[1]] for x in categories]

        # Make the bar plots
        width = 0.35
        p1 = pylab.bar([x for x in range(len(categories))], female, width=width)
        p2 = pylab.bar([x + width for x in range(len(categories))], male, width=width)
        pylab.legend((p1[0], p2[0]), gender)

        pylab.title(title)
        pylab.xlabel('Age Group')
        pylab.ylabel('Population with Diabetes')

        # Place the tick between both bar plots
        pylab.xticks([x + width / 2 for x in range(len(categories))], categories, rotation='vertical')
        pylab.show()
        # optionally save the plot to a file; file extension determines file type
        # pylab.savefig("plot_bar.png")

    elif plot_type == 'PIE':

        # total population with diabetes per gender
        male = sum([data[x][gender[1]] for x in categories])
        female = sum([data[x][gender[0]] for x in categories])

        pylab.title(title)
        pylab.pie([female, male], labels=gender, autopct='%1.1f%%')
        pylab.show()
        # optionally save the plot to a file; file extension determines file type
        # pylab.savefig("plot_pie.png")


def main():
    # Opens the file as fp
    fp = open_file()
    # data is the initial dictionary created from the file
    data = create_dictionary(fp)

    print("\n                Region Codes\n"
          "    MENA: Middle East and North Africa\n"
          "    EUR: Europe\n"
          "    AFR: Africa\n"
          "    NAC: North America and Caribbean\n"
          "    SACA: South and Central America\n"
          "    WP: Western Pacific\n"
          "    SEA: South East Asia\n")

    # Region is the input of the code for the continent
    region = input("Enter region code ('quit' to terminate): ")

    # While the input is not "quit"
    while region.lower() != "quit":
        # If the region inputted is in regions then the following code will run
        if(region.upper() in REGIONS)==True:

            # Data2 is the country totals from the get_country_total function
            data2 = get_country_total(data[region.upper()])
            # Displays the table
            display_table(data2, region)

            # Index one is total diabetes population and total population
            totals = [0,0]
            for c,d in data2.items():
                totals[0] += d[0]
                totals[1] += d[1]

            print("\n{:<25s}{:>20,d}{:>16,d}\n".format("TOTAL", totals[0], totals[1]))

            # Plots the data
            if input("Do you want to visualize diabetes prevalence by age group and gender (yes/no)? ").lower() == "yes":

                data_for_plot = prepare_plot(data[region.upper()])
                plot_data("PIE", data_for_plot, REGIONS[region.upper()])
                plot_data("BAR", data_for_plot, REGIONS[region.upper()])

            print("\n                Region Codes\n"
                  "    MENA: Middle East and North Africa\n"
                  "    EUR: Europe\n"
                  "    AFR: Africa\n"
                  "    NAC: North America and Caribbean\n"
                  "    SACA: South and Central America\n"
                  "    WP: Western Pacific\n"
                  "    SEA: South East Asia\n")

            region = input("Enter region code ('quit' to terminate): ")

        # Asks for the region code again, if it does not exist in the regions dict
        elif region.lower() != "quit" and (region.upper() not in REGIONS) == True:
            print("Error with the region key! Try another region")
            print("\n                Region Codes\n"
                      "    MENA: Middle East and North Africa\n"
                      "    EUR: Europe\n"
                      "    AFR: Africa\n"
                      "    NAC: North America and Caribbean\n"
                      "    SACA: South and Central America\n"
                      "    WP: Western Pacific\n"
                      "    SEA: South East Asia\n")
            region = input("Enter region code ('quit' to terminate): ")

        #Breaks if quit
        elif region.lower() == "quit" and (region.upper() not in REGIONS) == True:
            break

###### Main Code ######
if __name__ == "__main__":
    main()