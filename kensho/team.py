data_infrastructure = [
  "alexp",
  "brian.stearns"
]

query_infrastructure = [
  "predrag",
  "pedro.mantica",
  "bojan",
  "michaela"
]

ml_infrastructure = [
  "lee.bernick",
  "meher.islam",
  "hamzah.qudsi"
]

data_implementation = [
  "ben",
  "hamima.halim",
  "anurag.rai",
  "hossein.moein",
  "luke.brown",
  "joseph.bylund"
]

team = (
  ["charles.ponti", "leonid"] 
  + data_infrastructure 
  + query_infrastructure
  + ml_infrastructure
  + data_implementation
)

query = f"AND assignee in {team}"

for member in team:
  print(member)