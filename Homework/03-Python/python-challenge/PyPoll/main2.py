# import the os module
import os

# Module for reading CSV files
import csv

#set uo the cvs file path
election_csv = os.path.join('Resources', 'election_data.csv')

# set up the initial number
count1 = 0
count2 = 0
count3 = 0
count4 = 0
total = 0

# Open CSV file
with open(election_csv, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:  

        total += 1
        if  row[2] == "Khan":
            count1 += 1
        
        elif row[2] == "Correy" :
            count2 += 1
           
        elif row[2] == "Li":
            count3 += 1
        
        else:
            count4 += 1
    
    # caculate percentage of each
    Total_votes = count1 + count2 + count3 + count4
    count1_percentage = f"{(count1/Total_votes):.3%}"
    count2_percentage = f"{(count2/Total_votes):.3%}"
    count3_percentage = f"{(count3/Total_votes):.3%}"
    count4_percentage = f"{(count4/Total_votes):.3%}"    

    # format the () 
    sign1 = r"("
    sign2 = r")"
    
    # find the winner
    winner = max(count1, count2, count3, count4)
    #winner_name = 
    
    print("Election Results")
    print ("------------------------------")
    print(f"Total Votes:  {str(Total_votes)}")
    print ("------------------------------")
    print (f"Khan: {str(count1_percentage)}  {str(sign1)}{str(count1)}{str(sign2)}" )
    print (f"Correy: {str(count2_percentage)}  {str(sign1)}{str(count2)}{str(sign2)}" )    
    print (f"Li: {str(count3_percentage)}  {str(sign1)}{str(count3)}{str(sign2)}" )    
    print (f"O'Tooley: {str(count4_percentage)}  {str(sign1)}{str(count4)}{str(sign2)}" )        
    print ("------------------------------")
    print(f"Winner: Khan {str(winner)}")

# Set variable for output file
output_file = os.path.join("output","PyPoll.txt")
with open(output_path, 'w', newline='') as txtfile:
    csvwriter = csv.writer(csvfile, delimiter=',')