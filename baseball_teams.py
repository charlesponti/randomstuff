import functools

teams = [
    {
        'league': 'National League',
        'division': 'East',
        'teams': [
            {'name': 'Atlanta Braves'},
            {'name': 'Miami Marlins'},
            {'name': 'New York Mets'},
            {'name': 'Philadelphia Phillies'},
            {'name': 'Washington Nationals'},
        ]
    },
    {
        'league': 'National League',
        'division': 'Central',
        'teams': [
            {'name': 'Chicago Cubs'},
            {'name': 'Cincinnati Reds'},
            {'name': 'Milwaukee Brewers'},
            {'name': 'Pittsburgh Pirates'},
            {'name': 'St. Louis Cardinals'},
        ]
    },
    {
        'league': 'National League',
        'division': 'West',
        'teams': [
            {'name': 'Arizona Diamondbacks'},
            {'name': 'Colorado Rockies'},
            {'name': 'Los Angeles Dodgers'},
            {'name': 'San Diego Padres'},
            {'name': 'San Francisco Giants'},
        ]
    },
    {
        'name': 'American League',
        'division': 'East',
        'teams': [
            {'name': 'Baltimore Orioles'},
            {'name': 'Boston Red Sox'},
            {'name': 'New York Yankees'},
            {'name': 'Tampa Bay Rays'},
            {'name': 'Toronto Blue Jays'},
        ]
    },
    {
        'name': 'American League',
        'division': 'Central',
        'teams': [
            {'name': 'Chicago White Sox'},
            {'name': 'Cleveland Indians'},
            {'name': 'Detroit Tigers'},
            {'name': 'Kansas City Royals'},
            {'name': 'Minnesota Twins'},
        ]
    },
    {
        'name': 'American League',
        'division': 'West',
        'teams': [
            {'name': 'Houston Astros'},
            {'name': 'Los Angeles Angels'},
            {'name': 'Oakland Athletics'},
            {'name': 'Seattle Mariners'},
            {'name': 'Texas Rangers'},
        ]
    },
]

def append_teams(initial, current_item):
  for team in current_item['teams']:
    initial.append(team)
  return initial

def get_teams():
  return functools.reduce(append_teams, teams, [])