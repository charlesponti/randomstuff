class DB:
    def __init__(self):
        self.table = {}
        self.amount = 0

    def get_card_balance(self, card_number: int) -> int:
        """
        This is an example of Google style.

        Args:
            param1: This is the first param.
            param2: This is a second param.

        Returns:
            This is a description of what is returned.

        Raises:
            KeyError: Raises an exception.
        """
        return self.amount

    def deduct_from_card(self, amount=0) -> DB:
        self.amount -= amount
        return self


db = DB()

def charge_card(card_number, amount):
    has_enough_funds = db.get_card_balance(card_number) > amount
    if has_enough_funds:
        db.deduct_from_card(card_number, amount)


def send_tip_to_service_worker_fund(amount):
    pass


def add_tip(card_number, transaction):
    total = transaction.total
    charge_card(card_number, total + 5.00)  # Add 5 dollars to total to account for tip
    send_tip_to_service_worker_fund()  # Send tip to Service Workers Fund
