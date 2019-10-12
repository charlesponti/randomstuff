from flask import Flask
from topics.pandas import transactions

app = Flask(__name__)

@app.route('/')
def get(**args):
  return transactions.to_json()

@app.route('/transactions/<account>')
def get_by_amount(account: str):
  print(account)
  return transactions.query(f"Account Name == {account}")

if __name__ == "__main__":
  app.run(host='localhost', port=config.PORT, debug=config.DEBUG_MODE)