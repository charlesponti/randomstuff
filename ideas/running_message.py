import sys


def return_message(miles, total_time):
    time_per_mile = miles / total_time
    print(
        f"I went for a run today. I did {miles} miles in {total_time} ({time_per_mile})"
    )


if __name__ == "__main__":
    return_message()
