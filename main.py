# import matplotlib.pyplot as plt

# year = [1950, 1970, 1990, 2010]
# population = [2.3, 4.1, 5.9, 7.1]

# plt.scatter(year, population)

# plt.show()
import pandas as pd
import csv
import json
from flask import Flask, Request, Response

app = Flask(__name__, static_folder='./app/build')



# text = open('./data/transactions.csv', 'r')
transactions = pd.read_csv('./data/transactions.csv', delimiter=',', header=0)

@app.route('/')
def get(**args):
  return transactions.to_json()

@app.route('/transactions')
def get_by_amount():
  return transactions.query(f"Amount > {args}")

if __name__ == "__main__":
  app.run(host='localhost', port='5000', debug=True)

