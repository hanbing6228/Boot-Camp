# import the os module
import os

# Module for reading CSV files
import csv

#set uo the cvs file path
election_csv = os.path.join('Resources', 'election_data.csv')
# Open CSV file
with open(election_csv, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    name_votes = {}
    total_votes = 0
    winner = str()
    # Read each row of data after the header
    for row in csvreader:  
        total_votes += 1
        name = row[2]
        if name in name_votes:
            votes = name_votes.get(name)
            name_votes.update({name : votes + 1})
        else:
            name_votes.update({name : 1})
    #print("name_votes")
    
    for keys, values in name_votes.items():
        print(keys + ": " +  str(round(values/total_votes*100, 5))  + "% (" + str(values) + ")")
        
    winner = ""
    max_votes = 0
    i = 0
    for keys, values in name_votes.items():
        if i == 0:
            winner = keys
            max_votes = values
            i += 1
        else:
            if values > max_votes:
                winner = keys
    
    output_file = open("output.txt", "w")
    print("Election Results", file = output_file)
    print (f"------------------------------", file = output_file)
    print (f"Total Votes:" ,total_votes, file = output_file)
    print ("------------------------------", file = output_file)    
    print(keys + ": " +  str(round(values/total_votes*100, 5))  + "% (" + str(values) + ")", file = output_file)
    print ("------------------------------", file = output_file)
    print ("Winner:" + winner, file = output_file)
    print ("------------------------------", file = output_file)

    output_file.close()