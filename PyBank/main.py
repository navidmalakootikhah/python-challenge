#Creating my PyBank Python

#Importing os and CSV

import os
import csv

# Declaring variable
sum=0
count=0
sumchange=0
dictionary={}
changedict={}
profloss=[]
changes=[]
month=[]
i=0
change=0

#Opening and reading the file
banking_info= os.path.join('..', 'Resources', 'budget_data.csv')
with open(banking_info, 'r')as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
   
   #Adding all data into a dictionary and proffit/loss into a list
    for row in csvreader:
      count=count+1
      sum=sum+int(row[1])
      dictionary.update({row[0]:row[1]})
      profloss.append(int(row[1]))
      month.append(str(row[0]))
    #Claculating changes and storing them in a dictionary of month and change
    while i<(len(profloss)-1):
      change = profloss[i+1] - profloss[i]
      changes.append(change)
      changedict.update({month[i+1]:changes[i]})
      i=i+1
    #Calculating average, max and min changes
    for change in changes:
      sumchange=sumchange+change
    average=sumchange/len(changes)
    maxchangemonth=max(changedict,key=changedict.get)
    minchangemonth=min(changedict,key=changedict.get)
    maxchange=max(changedict.values())
    minchange=min(changedict.values())

print(f"Total Month: {count}")
print(f"Total: ${sumchange}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {maxchangemonth} (${maxchange})")
print(f"Greatest Increase in Profits: {minchangemonth} (${minchange})")
 
#Writing the results to a file

output_path = os.path.join("..", "Resources", "PyBank.csv")
with open(output_path, 'w', newline='') as datafile:

    # Initialize csv.writer
    csvwriter = csv.writer(datafile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Month', 'Total $', 'Average Change', 'Greatest Increase in Profits Month','Greatest Increase in Profits', 'Greatest Decrease in Profits Month', 'Greatest Decrease in Profits'])

    # Write the second row
    csvwriter.writerow([count, sumchange, average, maxchangemonth, maxchange, minchangemonth, minchange])
