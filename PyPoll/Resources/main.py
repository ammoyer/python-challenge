import os 
import csv 

electioncsv = os.path.join("PyPoll/Resources/election_data.csv")

totalvotes = 0    
candidate_votes = {}

with open (electioncsv) as electiondata:
    reader = csv.reader(electiondata)
    header = next(electiondata)
    print(header)


#The total number of votes cast
    for row in reader:
        candidate = row[2]
        totalvotes = totalvotes + 1 

        if candidate in candidate_votes.keys():
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1


#The winner of the election based on popular vote.
for key in candidate_votes.keys():
    if candidate_votes[key] == max(candidate_votes.values()):
        winner = key


print("Election Results")
print("------------------------")
print(f"Total Votes: {totalvotes}")  
print("--------------------------------")
percent = []
for i in candidate_votes.keys():
    percent = round(candidate_votes[i]/totalvotes*100, 2)
    poll_results = f"Percentage of Votes Each Candidate Won: {i}: {percent} %: ({candidate_votes[i]})"
    print(poll_results)
print(f"Candidates Who Received Votes: {candidate_votes}")
#print(f"Percentage of Votes Each Candidate Won: {percent}")
print(f"The Winner is: {winner}.")


filepathtosave = ("analysis.txt")
with open(filepathtosave,'w') as text:
    text.write("-------------------------\n")
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {totalvotes}\n")
    text.write("-------------------------\n")
    text.write(f"{poll_results}\n")
    text.write(f"Candidates Who Received Votes: {candidate_votes}\n")
    text.write(f"The Winner is: {winner}.\n")
