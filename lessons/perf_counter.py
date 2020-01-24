"""Measuring time"""

from time import perf_counter


def upto_for(range_of_numbers: int):
    """Sum 1...n with a for loop"""
    total = 0
    for i in range(range_of_numbers):
        total += i
    return total


def upto_sum(length_of_range):
    return sum(range(length_of_range))


def get_performance(starttime: float) -> float:
    """Get performance relative to starttime"""
    return perf_counter() - starttime


def get_functon_performance(*args, **kwargs):
    # Capture current time
    starttime = perf_counter()

    # Execute function to measure performance
    args[0](args[1])

    # Get performance of function
    return get_performance(starttime)


length_of_range = 1_000_000

print(get_functon_performance(upto_for, length_of_range))
print(get_functon_performance(upto_sum, length_of_range))
