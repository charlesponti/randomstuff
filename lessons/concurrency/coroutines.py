from random import randint
import time
import asyncio


def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd


def main():
    odds1 = [odd for odd in odds(3, 15)]
    odds2 = tuple(odds(21, 29))


def randn():
    time.sleep(2)
    return randint(1, 10)


if __name__ == "__main__":
    main()
