import csv
import pandas as pd

fieldnames = [
    "Date",
    "Description",
    "Original Description",
    "Amount",
    "Transaction Type",
    "Category",
    "Account Name",
    "Labels",
    "Notes",
]


class Transaction:
    def __init__(self, *args, **kwargs):
        for fieldname, i in fieldnames:
            print(i, fieldname)


csvfile = open("./data/transactions.csv")

pandas_csv = pd.read_csv("./data/transactions.csv")


print(pandas_csv.query("Amount > 10000"))

reader = csv.DictReader(csvfile)

# Create Pandas DataFrame from DictReader
transactions = pd.DataFrame(reader)

csvfile.close()
