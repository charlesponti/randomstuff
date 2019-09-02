
class DB:
  get_card_balance():
    return 5

def get_card_balance():
  db.get_card_balance()

def charge_card(card_number, amount):
  has_enough_funds = get_card_balance(card_number) > amount
  if has_enough_funds:
    deduct_from_card(card_number, amount)
  else:
    raise NotEnoughFundError

# def send_tip_to_service_worker_fund(amount):

def add_tip(card_number, transaction):
  total = transaction.total
  charge_card(card_number, total + 5.00) # Add 5 dollars to total to account for tip
  send_tip_to_service_worker_fund() # Send tip to Service Workers Fund
