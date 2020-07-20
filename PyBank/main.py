

import os 
import csv

#Budget Data Pathway 
budgetcsv = os.path.join("PyBank/Resources/budget_data.csv")

total_months = 0 
netprofit_losses = 0
netchangelist = []
netchange = 0 
monthofchange = []
greatestincrease = ["", 0]
greatestdecrease = ["", 9999999999]

with open (budgetcsv) as budgetdata:
    reader = csv.reader(budgetdata)
    header = next(reader)
    jandata = next(reader)
    print(header)
    total_months = total_months + 1 
    netprofit_losses = netprofit_losses + int(jandata[1])
    previousvalue = int(jandata[1])

    for row in reader:
        total_months+=1
#print(total_months)
        netprofit_losses = netprofit_losses + int(row[1])

        netchange = int(row[1]) - previousvalue
        previousvalue = int(row[1])
        netchangelist = netchangelist + [netchange]
        monthofchange = monthofchange + [row[0]]
        if netchange > greatestincrease[1]: 
            greatestincrease[0] = row[0] 
            greatestincrease[1] = netchange
        if netchange < greatestdecrease[1]:
            greatestdecrease[0] = row[0]
            greatestdecrease[1] = netchange

netaverage = round(sum(netchangelist)/len(netchangelist), 2)

# The net total amount of "Profit/Losses" over the entire period
#netprofit_losses = 0
#for row in reader:
    #netprofit_losses = netprofit_losses + int(row[1])

#The average of the changes in "Profit/Losses" over the entire period
#change = 


#The greatest increase in profits (date and amount) over the entire period
#profit_increase = 


print("Financial Analysis")
print("-----------------------")
print("Total Months:" + str(total_months))
print("Net Total Amount of 'Profit/Losses':" + str(netprofit_losses))
print(f"Average of changes in Profit/Losses over the entire period: {netaverage}.")
print(f"Greatest increase in profits over the entire period: {greatestincrease[0]} {greatestincrease[1]}")
print(f"Greatest decrease in profits over the entire period: {greatestdecrease[0]} {greatestdecrease[1]}")


filepathtosave = ("PyBank/Resources/analysis.txt")
with open(filepathtosave,'w') as text:
    text.write("-------------------------\n")
    text.write("Financial Analysis\n")
    text.write("-------------------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write("-------------------------\n")
    text.write(f"Net Total Amount of Profit/Losses: {netprofit_losses}\n")
    text.write(f"Average of changes in Profit/Losses over the entire period: {netaverage}\n")
    text.write(f"Greatest increase in profits over the entire period: {greatestincrease[0]} {greatestincrease[1]}\n")
    text.write(f"Greatest decrease in profits over the entire period: {greatestdecrease[0]} {greatestdecrease[1]}\n")
