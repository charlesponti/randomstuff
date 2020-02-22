class PersonalFinance:
    """
    :param user_id: UUID of user
    :type  user_id:
    """

    user_id: int

    def __init__(self, user_id: int):
        super().__init__()
        self.user_id = user_id

    def purchase_percentage(self, salary: int, purchase_price: float) -> float:
        """
        While listening to the Dave Ramsey Show, he discussed how someone who
        earns $42,000,000 spending $100,000 is equivalent to someone who
        earns $42,000 spending $10. It can be very difficult for people to wrap
        their minds around large numbers such as this, so I wanted to create
        something that would help with this mental framing.

        :return: The percentage of the user's salary
        :type: float
        """
        percentage = purchase_price / salary * 100
        print(f"This purchase would be {percentage}%")
