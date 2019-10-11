import pandas as pd

with open('./data/transactions.csv') as csvfile:
  fieldnames = [
    "Date", "Description", "Original Description", "Amount",
    "Transaction Type", "Category", "Account Name", "Labels", "Notes"
  ]
  reader = csv.DictReader(csvfile, fieldnames=fieldnames)
  df = pd.DataFrame(reader)
  print(df)

transactions = pd.read_csv('./data/transactions.csv', delimiter=',', header=0)
