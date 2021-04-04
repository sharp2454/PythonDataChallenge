#import Modules
import os
import csv

#create file path
csvpath = os.path.join("Resources","election_data.csv")

with open (csvpath, "r") as csvfile:
 
    csvreader = csv.reader(csvfile, delimiter=',')
    #read the header row   
    csv_header = next(csvfile)
    first_row = next(csvreader)

    #print first row/test
    print(first_row)    
    #print header
    print(f"Header: {csv_header}")

#define variables
Candidates =[]
Votes_per_Candidate = []

