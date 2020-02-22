import functools
import json

# Teams
# | ID | team_name | city | state | league | division
class Team:
    def __init__(
        self,
        name: str = None,
        city: str = None,
        division: str = None,
        league: str = None,
        state: str = None,
    ):
        self.name = name
        self.division = division
        self.league = league
        self.city = city
        self.state = state


class Division:
    name: str = None
    teams = []

    def __init__(self, *args, **kwargs):
        self.league = kwargs.get("league")
        self.name = kwargs.get("name")


class League:
    name = None
    divisions: [Division] = []

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get("name")

    def add_division(self, division_name: str):
        if division_name not in self.divisions:
            self.divisions.append(division_name)


league_names = ["National", "American"]
division_names = ["East", "Central", "West"]


nl_east = [
    {"name": "Atlanta Braves"},
    {"name": "Miami Marlins"},
    {"name": "New York Mets"},
    {"name": "Philadelphia Phillies"},
    {"name": "Washington Nationals"},
]

nl_central = []

teams = [
    {
        "league": "National League",
        "divisions": [
            {
                "name": "Central",
                "teams": [
                    {"name": "Chicago Cubs"},
                    {"name": "Cincinnati Reds"},
                    {"name": "Milwaukee Brewers"},
                    {"name": "Pittsburgh Pirates"},
                    {"name": "St. Louis Cardinals"},
                ],
            },
            {
                "name": "West",
                "teams": [
                    {"name": "Arizona Diamondbacks"},
                    {"name": "Colorado Rockies"},
                    {"name": "Los Angeles Dodgers"},
                    {"name": "San Diego Padres"},
                    {"name": "San Francisco Giants"},
                ],
            },
        ],
    },
    {
        "name": "American League",
        "division": "East",
        "teams": [
            {"name": "Baltimore Orioles"},
            {"name": "Boston Red Sox"},
            {"name": "New York Yankees"},
            {"name": "Tampa Bay Rays"},
            {"name": "Toronto Blue Jays"},
        ],
    },
    {
        "name": "American League",
        "division": "Central",
        "teams": [
            {"name": "Chicago White Sox"},
            {"name": "Cleveland Indians"},
            {"name": "Detroit Tigers"},
            {"name": "Kansas City Royals"},
            {"name": "Minnesota Twins"},
        ],
    },
    {
        "name": "American League",
        "division": "West",
        "teams": [
            {"name": "Houston Astros"},
            {"name": "Los Angeles Angels"},
            {"name": "Oakland Athletics"},
            {"name": "Seattle Mariners"},
            {"name": "Texas Rangers"},
        ],
    },
]


def append_teams(initial, current_item):
    for team in current_item["teams"]:
        initial.append(team)
    return initial


def get_teams():
    return functools.reduce(append_teams, teams, [])


leagues = []

for league_name in league_names:
    league = League(name=league_name)

    for division_name in division_names:
        league.add_division(division_name)

    leagues.append(league)

print(json.dumps(leagues[0]))
