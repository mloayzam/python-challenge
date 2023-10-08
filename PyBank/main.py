#####Student: Mario Loayza - Data Analytics and Visualization Boot Camp 
####Module 3 Challenge (Python Challenge), main.py script for PyBANK folder: Finantial Analysis

# Import the os module
import os

# Module for reading CSV files
import csv

# Store filepath in a variable
csvpath = os.path.join('Resources', 'budget_data.csv')

# Lists to store data
date = []
PAL =  []
changes = []
# Open and read csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#Initiate Total variable
    total = 0
    
    # Read through each row of data after the header
    # Read each row of data after the header
    for row in csvreader:

      # Add  date and Profit/losses
       date.append(row[0])
       PAL.append(int(row[1]))
       total += int(row[1]) 
       
    # Calculate the changes in Profit/Losses and store in List changes
    for i in range(1, len(date)):
            change = PAL[i]-PAL[i-1]
            changes.append(change) 

    #Calculate the Average of changes, Maximum and Minimum of changes in Profit/Losses over the period
    Average = sum(changes)/len(changes)
    Max = max(changes)
    Min = min(changes)

    #index retur the numeric location of max and min values from changes list
    max_loc = changes.index(max(changes))
    min_loc = changes.index(min(changes))

# save the output file path
output_file = os.path.join('analysis','results.txt')

# open the output file and write the results including the date assoiciated with the max, min changes location
with open(output_file, "w", newline='') as datafile:
     datafile.write(f"Finantial Analysis\n")
     datafile.write(f"\n")
     datafile.write(f"------------------------\n")
     datafile.write(f"\n")
     datafile.write(f"Total Months:  {len(date)}\n")
     datafile.write(f"\n")
     datafile.write(f"Total amount of Profit/Losses over the entire period:  ${str(total)}\n")
     datafile.write(f"\n")
     datafile.write(f"Total average of the changes in Profit/Losses over the entire period:  ${str(round(Average,2))}\n")
     datafile.write(f"\n")
     datafile.write(f"The greatest increase in profits (date and amount) over the entire period: {date[max_loc +1]} (${str(Max)})\n")
     datafile.write(f"\n")
     datafile.write(f"The greatest decrease in profits (date and amount) over the entire period: {date[min_loc +1]} (${str(Min)})\n")

