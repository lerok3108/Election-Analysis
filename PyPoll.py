import csv
import os
file_to_load = ('Resources/election_results.csv')

# Open the election results and read the file
with open(file_to_load) as election_data:
    #to do:read and analyze the data here
    file_reader=csv.reader(election_data)

    #read and print the header row
    headers=next(file_reader) 
    print(headers)


# Create a filename variable to a direct or indirect path to the file.
file_to_save = ('Resources/election_analysis.txt')

# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the election\n---------------------------\nArapahoe\nDenver\nJefferson")
txt_file.close()




