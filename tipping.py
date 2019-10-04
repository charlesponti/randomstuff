from flask import Flask

app = Flask(__name__)

class DB:
  def __init__(self):
    self.table = {}

  def get_card_balance(self):
    return 5

  def deduct_from_card(self, amount=0):
    self.amount -= 0
    return self.amount
db = DB()

def charge_card(card_number, amount):
  has_enough_funds = db.get_card_balance(card_number) > amount
  if has_enough_funds:
    deduct_from_card(card_number, amount)
  else:
    raise NotEnoughFundsError

def send_tip_to_service_worker_fund(amount):


def add_tip(card_number, transaction):
  total = transaction.total
  charge_card(card_number, total + 5.00) # Add 5 dollars to total to account for tip
  send_tip_to_service_worker_fund() # Send tip to Service Workers Fund

if __name__ == 'main':
  app.run()