from json import JSONEncoder
from csv import DictReader, DictWriter
import pandas as pd
import numpy as np

person = pd.DataFrame({
  'name': ['Chase', 'Lucy'],
  'age': [33, 34],
  'hair': ['black', 'brown']
})


print(person)
