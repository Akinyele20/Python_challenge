# This my PyBank file
# Modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

print(csvpath)

# create variables
Total_months = 0
Net_total = 0


# ----------
# open csv files
# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read Header
     # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read through each row
    for row in csvreader:
        print(row)

        # Months +1
        Total_months += 1

        # Net Total + second;
        Net_total += int (row[1])

# output
# create a variable called output
output = (
    f"financial Analysis\n"
    f"--------------------\n"
    f"Total Months: {Total_months} \n"
    f"Total: {Net_total}  \n" 
    f"Average Change:  \n"
    f"Greatest Increase in Profits:  \n"
    f"Greates Decrease in Profits:  \n"
)

print(output)

# Export a text file
output_path = os.path.join(".", "Analysis", "budget_Analysis.txt")

with open(output_path, "w") as txt_file:
    txt_file.write(output)
 