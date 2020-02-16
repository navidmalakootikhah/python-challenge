#Importing os and CSV
import os
import csv
#Declare Variables
vote_count=0
sum_candidate=[]
candidate=[]
candidate_list=[]
percent=[]
m=0
j=0
n=0
x=0
dictionary={}
#Opening and reading the file to create a list of unique candidates and find the total votes
poll_info= os.path.join('..', 'Resources', 'election_data.csv')
with open(poll_info, 'r')as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        vote_count=vote_count+1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            sum_candidate.append(m)
#Opening and reading the file to create a list of sum of votes per candidate
with open(poll_info, 'r')as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        while int(m)<int(len(candidate_list)):
            #print(row[2])
            #print(candidate_list[m])
            if row[2]==candidate_list[m]:
                sum_candidate[m]=sum_candidate[m]+1
            m=m+1
        m=0
    #calculate percentage
    for num in sum_candidate:
        percent.append(round((int(num)/int(vote_count))*100))
    #create a dictionary of candidates and sum of votes per candidate
    while j<len(candidate_list):
        dictionary.update({candidate_list[j]:sum_candidate[j]})
        j=j+1
    #Printing results
    print("Election Results")
    print("--------------------------------------------")
    print(f"Total Votes: {vote_count}")
    print("--------------------------------------------")
    while n<len(candidate_list):
        print(f"{candidate_list[n]} : {percent[n]}% ({sum_candidate[n]})")
        n=n+1
    print("--------------------------------------------")
    winner=max(dictionary,key=dictionary.get)
    print(f"Winner: {winner}")
 
output_path = os.path.join("..", "Resources", "PyPoll.csv")
with open(output_path, 'w', newline='') as datafile:

    # Initialize csv.writer
    csvwriter = csv.writer(datafile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['Total Votes:',vote_count])
    csvwriter.writerow(['Name','Percent%','Vote Count'])

    while x<len(candidate_list):
        csvwriter.writerow([candidate_list[x],percent[x],sum_candidate[x]])
        x=x+1
    csvwriter.writerow(['','Winner:', winner])
    


