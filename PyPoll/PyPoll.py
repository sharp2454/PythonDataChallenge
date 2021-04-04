#import Modules
import os
import csv

#define variables
Candidates = []
Votes = []
TotalVotes = 0
TotalPercent = []
UniqueCandidates = []


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

  



    #read through the data after header
    for row in csvreader:
        
        #total votes
        TotalVotes += 1

        #append candidates
        if row[2] not in UniqueCandidates:
            UniqueCandidates.append(row[2])

        #make a new list
        Votes.append(row[2])    

    #read through the data and start tallying votes per candidate
    for Candidate in UniqueCandidates:
        Candidates.append(Votes.count(Candidate))  
        TotalPercent.append(round(Votes.count(Candidate)/TotalVotes*100,3))  

    #Return who has the most votes
    Winner = UniqueCandidates[Candidates.index(max(Candidates))] 

    #print summary
    print("Election Results")
    print("==========================")
    print(f"Total Votes: {TotalVotes}") 
    print("==========================")
    for x in range(len(UniqueCandidates)):
        print(f"{UniqueCandidates[x]}: {TotalPercent[x]}% {Candidates[x]}")
    print("==========================")
    print(f"Winner: {Winner}")   
    print("==========================") 


    #set path for Analysis file
    output_path = 'Output.txt'

    #open the output path
    with open(output_path, "w") as file:
    #write analysis to the output file
        file.write("Election Results")
        file.write("\n==========================")
        file.write(f"\nTotal Votes: {TotalVotes}")
        file.write("\n==========================")
        for x in range(len(UniqueCandidates)):
            file.write(f"\n{UniqueCandidates[x]}: {TotalPercent[x]}% {Candidates[x]}")
        file.write("\n==========================")
        file.write(f"\nWinner: {Winner}") 
        file.write("\n==========================")
    
    




