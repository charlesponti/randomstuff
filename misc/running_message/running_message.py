# Running Message

import sys


def return_message(miles, total_time):
    """
    The idea behind this came from wanting to share the details of my latest run
    with a friend. The current sharing options only allow for sharing a portion
    of the details and with an unuseful image. I wanted to think of ways that
    different options could be allowed for sharing with friends
    """
    time_per_mile = format(total_time / miles, '.2f')
    return f"I went for a run today. I did {format(miles, '.2f')} miles in {format(total_time, '.2f')} ({time_per_mile})"


if __name__ == "__main__":
    return_message()
