# import the os module
import os

# Module for reading CSV files
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')


#print (budget_csv)

print("Financial Analysis")

print ("-------------------------")

with open(budget_csv, newline="") as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    
    month = []

    Total = 0
    total_change = 0
    last_profit = 0 
    max_change = 0
    min_change = 0
    min_month =str()
    max_month =str()
    i = 0
    # Read each row of data after the header
    for row in csvreader:
        
        month.append(row[1])
        Total = Total + int(row[1])
        current_profit = int(row[1])
        if i == 0:
            last_profit = current_profit
            i = i + 1

        else:
            change = current_profit - last_profit
            total_change = total_change + change
            
            if max_change < change:
                max_change = change
                max_month = row[0]
            if min_change > change:
                min_change = change
                min_month = row[0]
            last_profit = current_profit



    output_file = open("output.txt", "w")    
    print('Total Months: ' ,len(month),file = output_file)
    print(f"Total:  ${Total:,.0f}", file = output_file)
    #print(f"Average Change: {str(Average)}")    
    print(f"Average Change: {str(total_change/85)}", file = output_file) 
    
    print(f"Greatest Increase in profits {str(max_month)} {str(max_change)}", file = output_file)
    print(f"Greatest Decrease in losses, {str(min_month)} {str(min_change)}", file = output_file)
    
    output_file.close()
    
