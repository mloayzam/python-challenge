#####Student: Mario Loayza - Data Analytics and Visualization Boot Camp 
####Module 3 Challenge (Python Challenge), main.py script for PyPOLL folder:Election Results

# Import the os module
import os

# Module for reading CSV files
import csv

# Store filepath in a variable
csvpath = os.path.join('Resources', 'election_data.csv')

# Create Lists to store data
ballotid = []
cand =  []
cand1 = []
cand2 = []
cand3 = []

# Open and read csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#create variables with the name of each candidate
    name1 = "Charles Casper Stockham"
    name2 = "Diana DeGette"
    name3 = "Raymon Anthony Doane"
    
    # Read through each row of data after the header
    # Read each row of data after the header
    for row in csvreader:

      # Add ballotid and candidates, len(ballodid) will be used for calculating the total number of votes cast
       ballotid.append(row[0])
       cand.append(str(row[2]))

# Loop through each candidate list (cand), conditional logic and add info to each candidate list name for calculate the total number of votes each candidate won
for cands in cand:
    if cands == name1:
         cand1.append(cands)

for cands in cand:
    if cands == name2:
         cand2.append(cands)

for cands in cand:
    if cands == name3:
         cand3.append(cands)

# Calculation of The percentage of votes each candidate won 
percand1 = (len(cand1)/len(ballotid))*100

percand2 = (len(cand2)/len(ballotid))*100

percand3 = (len(cand3)/len(ballotid))*100

# Condition for calculating the winner of the election based on popular vote 
if (percand1 > percand2 and percand1 > percand3):
        winner = name1
       
elif (percand2 > percand1 and percand2 > percand3):
        winner = name2
        
else:
        winner = name3


# save the output file path
output_file = os.path.join('analysis','results.txt')

# open the output file and write the results
with open(output_file, "w", newline='') as datafile:
     datafile.write(f"Election Results\n")
     datafile.write(f"\n")
     datafile.write(f"------------------------\n")
     datafile.write(f"\n")
     datafile.write(f"Total Votes:  {len(ballotid)}\n")
     datafile.write(f"\n")
     datafile.write(f"------------------------\n")
     datafile.write(f"\n")
     datafile.write(f"{name1}: {str(round(percand1,3))}% ({len(cand1)})\n")
     datafile.write(f"\n")
     datafile.write(f"{name2}: {str(round(percand2,3))}% ({len(cand2)})\n")
     datafile.write(f"\n")
     datafile.write(f"{name3}: {str(round(percand3,3))}% ({len(cand3)})\n")
     datafile.write(f"\n")
     datafile.write(f"------------------------\n")
     datafile.write(f"\n")
     datafile.write(f"Winner: {winner}\n")
     datafile.write(f"\n")
     datafile.write(f"------------------------\n")


