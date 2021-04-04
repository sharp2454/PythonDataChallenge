#import Modules
import os
import csv

#read csv file & separate the data into two lists
Months = []
Profits = []
Dates= []

csvpath = os.path.join("Resources","budget_data.csv")

with open (csvpath, "r") as csvfile:
 
    csvreader = csv.reader(csvfile, delimiter=',')
    #read the header row   
    csv_header = next(csvfile)
    first_row = next(csvreader)

    #print first row/test
    print(first_row)    

    #read each row of data after header
    for row in csvreader:
        Months.append(row[0])
        Profits.append(float(row[1]))

#Set variables for analysis  
MaxIncreaseIndex = 1
MaxDecreaseIndex= 1
Counter = 1
MaxIncrease = 0.0
MaxDecrease = 0.0
ProfitDelta = 0.0
ProfitDeltaTotal = 0.0

#Run through profits list starting at 1 to calculate delta from previous month
while Counter < (len(Profits)):
    ProfitDelta = (Profits[Counter] - Profits[Counter - 1])
    ProfitDeltaTotal += ProfitDelta

#Find greatest increase & decrease in profits & record the index
    if  ProfitDelta > MaxIncrease:
        MaxIncrease = ProfitDelta
        MaxIncreaseIndex = Counter
    elif  ProfitDelta < MaxDecrease:
          MaxDecrease = ProfitDelta
          MaxDecreaseIndex = Counter

    Counter +=1

#print analysis
print("Financial Analysis")
print("======================================")  
print(f"Total Months: {Counter}")
print(f"Total Profits: ${int(sum(Profits))}")
print(f"Average Change: ${round(ProfitDeltaTotal/(Counter - 1),2)}")
print(f"Greatest Increase in Profits: {Months[MaxIncreaseIndex]} (${(MaxIncrease):.2f})")
print(f"Greatest Decrease in Profits: {Months[MaxDecreaseIndex]} (${(MaxDecrease):.2f})")

#set path for Analysis file
output_path = 'Output.txt'

#open the output path
with open(output_path, "w") as file:
    #write analysis to the output file
    file.write("Financial Analysis\n")
    file.write("======================================\n")
    file.write(f"Total Months: {Counter}\n")
    file.write(f"Total Profits: ${int(sum(Profits))}\n")
    file.write(f"Average Change: ${round(ProfitDeltaTotal/(Counter - 1),2)}\n")
    file.write(f"Greatest Increase in Profits: {Months[MaxIncreaseIndex]} (${(MaxIncrease):.2f})\n")
    file.write(f"Greatest Decrease in Profits: {Months[MaxDecreaseIndex]} (${(MaxDecrease):.2f})\n")
    









      

