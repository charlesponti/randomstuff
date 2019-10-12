"""
This file shows how to define and use a function decorator
"""

def transaction_closure(fn):
  def wrapper(value, **kwargs):
    if not value:
      raise Exception(f"{value} is not truthy")
    return fn(value, **kwargs)
  return wrapper

@transaction_closure
def some_function(value):
  print(f"{value} is truthy")

some_function("Whattttt")
some_function(15)
some_function(True)