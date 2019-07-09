#import the os module
import os

# Module for reading CSV files
import csv

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')


print (budget_csv)

print("Financial Analysis")

print ("-------------------------")

with open(budget_csv, newline="") as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    # Read each row of data after the header
    #Total_months = len(csvfile.readlines())
    #Total_amount = sum(csvfile.readlines())
    #Average_Changes = Total_amount/Total_amount

    #print(f"Total months:" Total_months)
    #print("Total:" Total_amount)
    #print("Average Change:" Average_Changes)
    #print(csvreader)

    
    # Read each row of data after the header
    #for row in csvreader:
        #print(row)
    #print(len(f.readlines()))

#for row in csvreader:
        #if row[i] > row[i+1]:
            #print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

            # BONUS: Set variable to confirm we have found the video
            #found = True

            # BONUS: Stop at first results to avoid duplicates
            #break

    # If the video is never found, alert the user
    #if found is False:
        #print("Sorry about this, we don't seem to have what you are looking for!")

#Max_Increase = float("inf")
#Max_Decrease = -float("inf")
#Max_Increase_data = inf
#Max_Decrease_data = inf

#count_min = 0
#count_max = 0
#for i in Profit/Losses:
 #if i < Max_Increase:
 #max_Increase = i
 #count_min = 1
 #elif val == min_val:
 #count_min += 1
 #if i> Max_Decrease:
 #Max_Decrease = i
#count_max = 1
 #elif val == max_val:
 #count_max += 1
#print"Greatest Increase in Profits:", Max_Increase_data (Max_Increase)
#print"Greatest Decrease in Profits:", Max_decrease_data (Max_Decrease)

#def largestState():
    #INPUT = "statepopulations.csv"
    #COLUMN = 5
    #with open(INPUT, "rU") as csvFile:
        #data = csv.reader(csvFile)
        #next(data, None)
    #return max(data, key=lambda _: _[COLUMN])