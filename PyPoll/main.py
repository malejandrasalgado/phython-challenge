# Import the file
import csv
# Create a subroutine for printing 
def print_terminal_file(outfile,outline):
    print(outline)
    outfile.write(f'{outline}\n')

import os

myfile = os.path.dirname(__file__) + '\\Resources\\02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv'

# Open the csv
with open (myfile)as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',') 

 
    # Assign values to variables with descriptive names 
    votes=float(0)
    winner=""
    mostvotes=(0)
    headerrow = True

    # Loop through the election data and create the dictionary
    vote_dict={}

    for row in csvreader:
        if not headerrow:
            votes += 1
            if row[2] not in vote_dict:
                vote_dict[row[2]]= 1
            else:
                vote_dict[row[2]]+=1
        else:
            headerrow = False

    print(vote_dict)

# Open a text file for writing and reading
resultsfile = open(os.path.dirname(__file__) + "\\Analysis\\PyPollresults.txt","w+")
# Results show in the text file  
outputline='Election Results'
print_terminal_file(resultsfile,outputline)
outputline='-----------------------'
print_terminal_file(resultsfile,outputline)
outputline= f'Total Votes: {round(votes)}'
print_terminal_file(resultsfile,outputline)
outputline='-----------------------'
print_terminal_file(resultsfile,outputline)


# create a loop for to go throug the dictionary to calculate percentages by candidate 
for candidate, totalvotes in vote_dict.items():
    perc=float(totalvotes)/votes
    outputline=f'{candidate}: {perc:.3%} ({totalvotes})'
    print_terminal_file(resultsfile,outputline)
    if totalvotes>mostvotes:
        mostvotes=totalvotes
        winner=candidate


outputline='-----------------------'
print_terminal_file(resultsfile,outputline)
outputline=f'Winner: {winner}'
print_terminal_file(resultsfile,outputline)
outputline='-----------------------'
print_terminal_file(resultsfile,outputline)

csv_file.close()
resultsfile.close()













