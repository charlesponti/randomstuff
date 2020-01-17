# While listening to the Dave Ramsey Show, he discussed how someone who
# earns $42,000,000 spending $100,000 is equivalent to someone who
# earns $42,000 spending $10. It can be very difficult for people to wrap
# their minds around large numbers such as this, so I wanted to create
# something that would help with this mental framing.

def how_much_for_me(salary: int, purchase_price: float):
    # The percentage of your salary
    percentage = purchase_price / salary * 100
    print(f"This purchase would be {percentage}%")

if __name__ == '__main__':
    how_much_for_me(42_000_000, 10_000)