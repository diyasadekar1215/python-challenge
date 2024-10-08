
import os, csv
from pathlib import Path 

input_file = Path("/Users/diyasadekar/Downloads/Starter_Code 4/PyBank/Resources/budget_data.csv")

# Create empty lists to iterate through specific rows for the following variables
total_months = []
total_profit = []
monthly_profit_change = []
 
# Open csv in default read mode with context manager
with open(input_file,newline="", encoding="utf-8") as budget:

    # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget,delimiter=",") 

    # Skip the header labels to iterate with the values
    header = next(csvreader)  

    # Iterate through the rows in the stored file contents
    for row in csvreader: 

        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Obtain the max and min of the the monthly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
max_increase_month = monthly_profit_change.index(max_increase_value) + 1
max_decrease_month = monthly_profit_change.index(max_decrease_value) + 1 

# Print Statements
print("Financial Analysis")
print("----------------------------")
print(f"File Analyzed: {input_file}")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output_file = Path("/Users/diyasadekar/Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    
    # Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"File Analyzed: {input_file}\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total: ${sum(total_profit)}\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n")

print(f"\nAnalysis saved to: {output_file}")
