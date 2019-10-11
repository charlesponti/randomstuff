import csv
import pandas as pd

csvfile = open('./data/transactions.csv')

fieldnames = [
  "Date", "Description", "Original Description", "Amount",
  "Transaction Type", "Category", "Account Name", "Labels", "Notes"
]

reader = csv.DictReader(csvfile)

transactions = pd.DataFrame(reader)

print(transactions.query('Amount >= 10000'))

csvfile.close()
