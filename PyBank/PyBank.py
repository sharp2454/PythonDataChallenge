#import Modules
import os
import csv

#read csv file & separate the data into two lists
Months = []
Profits = []
Dates= []

csvpath = os.path.join(".Resources/budget_data.csv")

with open (csvpath, "r") as csvfile:
 
    csvreader = csv.reader(csvfile, delimiter=',')
    #read the header row   
    csv_header = next(csvfile)
    first_row = next(csvreader)

    #print first row/test
    print(first_row)    

    #read each row of data after header
    for row in csvreader:
        Months += 1
        Dates.append(row[0])
        Profits.append(float(row[1]))

#Set variables for analysis  
TotalChanges = 0 
ProfitTotal = Profits[0]
MaxIncrease = 0.0
MaxDecrease = 0.0


#Run through profits list starting at 1 to calculate delta from previous month
for x in range (1, Months):
    ProfitTotal += Profits[x]

    CurrentChange = Profits[x] - Profits[x-1]
    TotalChanges += CurrentChange

#Find greatest increase & decrease in profits & record the index
    if  CurrentChange > MaxIncrease:
        MaxIncrease = CurrentChange
        MaxIncreaseDate = Dates[x]
    elif  CurrentChange < MaxDecrease:
          MaxDecrease = CurrentChange
          MaxDecreaseDate = Dates[x]

    Counter +=1

#print analysis
print("Financial Analysis")
print("======================================")  
print(f"Total Months: {Months}")
print(f"Total Profits: ${(TotalProfits):.2f}")
print(f"Average Change: ${(TotalChanges/(Months - 1)):.2f}")
print(f"Greatest Increase in Profits: {MaxIncreaseDate} (${(MaxIncrease):.2f})")
print(f"Greatest Decrease in Profits: {MaxDecreaseDate} (${(MaxDecrease):.2f})")

#set path for Analysis file
output_path = 'Analysis.txt'

#open the output path
with open(output_path, "w") as file:
    #write analysis to the output file
    file.write("Financial Analysis\n")
    file.write("======================================\n")
    file.write(f"Total Months: {Months}\n")
    file.write(f"Total Profits: ${(TotalProfits)}\n")
    file.write(f"Average Change: ${(TotalChanges/(Months - 1)):.2f}\n")
    file.write(f"Greatest Increase in Profits: {MaxIncreaseDate} (${(MaxIncrease):.2f})\n")
    file.write(f"Greatest Decrease in Profits: {MaxDecreaseDate} (${(MaxDecrease):.2f})\n")
    









      

