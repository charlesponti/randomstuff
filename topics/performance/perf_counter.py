"""Measuring time"""

from time import perf_counter

def upto_for(n: int):
  """Sum 1...n with a for loop"""
  total = 0
  for i in range(n):
    total += i
  return total

def upto_sum(n):
  return sum(range(n))

i = 1_000_000

starttime = perf_counter()
upto_for(i)
duration1 = perf_counter() - starttime
print(duration1)

starttime2 = perf_counter()
upto_sum(i)
duration2 = perf_counter() - starttime2
print(duration2)