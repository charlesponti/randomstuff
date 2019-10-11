from flask import Flask
from topics.pyspark import transactions

app = Flask(__name__)

@app.route('/')
def get(**args):
  return transactions[:3]['Amount'].to_json()

@app.route('/transactions')
def get_by_amount(**args):
  return transactions.query(f"Amount > {args}")

if __name__ == "__main__":
  app.run(host='localhost', port='5000', debug=True)

