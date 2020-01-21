from typing import List
import json
from csv import DictReader, DictWriter
import sys
from getopt import getopt, GetoptError

data = None
file = None
transactions = []

def get_arguments(unixOptions: str, gnuOptions):
    try:
        return getopt(sys.argv[1:], unixOptions, gnuOptions)
    except GetoptError as err:
        print(f"Error getting arguments: {err}")

options, arguments = get_arguments("f:", ["file"])

for opt, arg in options:
    if (opt == "-f"):
        file = arg

if file:
    with open(file, "r") as file:
        data = DictReader(file)

        print(data.fieldnames)
        for row in data:
            transaction = dict(row)
            date: str = transaction["Date"]
            date_parts = date.split("/")
            transaction["Date"] = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"
            transactions.append(transaction)

    with open("./fixed-transactions.csv", "w") as file:
        writer = DictWriter(file, data.fieldnames)
        writer.writeheader()
        writer.writerows(transactions)
    print(len(transactions))
    print(transactions[-1])