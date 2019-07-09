# import the os module
import os

# Module for reading CSV files
import csv

#set uo the cvs file path
election_csv = os.path.join('Resources', 'election_data.csv')

#def result_data = (election_data):
    #name = str(election_data[0])
    #percentage = float(election_data[1])
    #total_votes1 = int(election_data[2])


# Read in the CSV file
with open(election_csv, newline="") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    name_list = []
    total_votes = 0
    for row in csvreader:
        name_list.append(row[2])
        name_list1 =set(name_list)
        total_votes = len(name_list1)
    print(total_votes)
    print(name_list1)


    
    
    #print("Election Results")
    #print ("------------------------------")
    #print(f"Total Votes:  {str(Total_votes)}")
    #print ("------------------------------")
    #print (f"Khan: {str(count1_percentage)}  {str(sign1)}{str(count1)}{str(sign2)}" )
    #print (f"Correy: {str(count2_percentage)}  {str(sign1)}{str(count2)}{str(sign2)}" )    
    #print (f"Li: {str(count3_percentage)}  {str(sign1)}{str(count3)}{str(sign2)}" )    
    #print (f"O'Tooley: {str(count4_percentage)}  {str(sign1)}{str(count4)}{str(sign2)}" )        
    #print ("------------------------------")
    #print(f"Winner:  {str(winner)}")