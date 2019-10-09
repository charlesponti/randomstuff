import matplotlib.pyplot as plt
import pandas as pd

transactions = pd.read_csv('./data/transactions.csv', delimiter=',')

def get_amount_date_tuple(transaction):
    print(type(transaction))
    return transaction['Amount'], transaction['Date']


amount_dates = transactions.applymap(
  get_amount_date_tuple
)

print(amount_dates)
year = [1950, 1970, 1990, 2010]
population = [2.3, 4.1, 5.9, 7.1]

plt.scatter(year, population)

plt.show()
