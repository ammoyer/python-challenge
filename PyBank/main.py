

import os 
import csv

#Budget Data Pathway 
budgetcsv = os.path.join("PyBank/Resources/budget_data.csv")

with open (budgetcsv) as budgetdata:
    reader = csv.reader(budgetdata)
    header = next(budgetdata)
    print(header)




