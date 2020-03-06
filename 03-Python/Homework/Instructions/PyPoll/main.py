#imports
import csv
import pandas as pd
import numpy as np

#read the csv file using pandas read_csv function
df_csv = pd.read_csv('./Resources/election_data.csv')

#create a DataFrame object
df = pd.DataFrame(df_csv)
#print(df)

#total number of votes cast
totalVotes = len(df)

#complete list of candidates who received votes
totalCandidates = 0
totalCandidates = len(df.drop_duplicates('Candidate'))


name = ""
votes = 0
percentage = 0
winner = ""

def voting():
    n = 0
    for item in df.iterrows():
        if (n < totalCandidates):
            name = df.drop_duplicates('Candidate').iloc[n, 2]   #all duplicates are removed in Candidate column. n is row, 2 is Cadidate col
            
            votes = df['Candidate'].value_counts().to_dict()
            votes = votes[name]
            percentage = votes / totalVotes
            n = n+1                                             #n is incremented to prepare for next loop

            print(name + ": " + '{:.3%}'.format(percentage) + "\t (" + str(votes) + ")")

            if(n == totalCandidates):
                return
    

winner = df['Candidate'].value_counts().idxmax()

def printResults(totalVotes, winner):
    print("Election Results")
    print("-------------------------------")
    print("Total Votes: " + str(totalVotes))
    print("-------------------------------")
    voting()
    print("-------------------------------")
    print("Winner: " + winner)
    print("-------------------------------")

printResults(totalVotes, winner)



