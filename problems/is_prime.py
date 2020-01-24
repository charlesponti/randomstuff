import pandas as pd


def is_prime(num: int) -> bool:
    for i in range(1, num):
        print("num", num)
        print("i", i)
        print("remainder", num % i)
        print("")

    return False


print(is_prime(3))
