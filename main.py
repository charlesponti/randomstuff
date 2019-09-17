from baseball_teams import get_teams
from functools import reduce

for team in get_teams():
  print(team['name'])
