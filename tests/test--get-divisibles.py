import getopt, sys

# read commandline arguments, first
fullCmdArguments = sys.argv

# - further arguments
argumentList = fullCmdArguments[1:]

unixOptions = ["hvs:"]
gnuOptions = ["help", "start", "end", "verbose"]

try:
  arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
  print(str(err))
  sys.exit(2)

for currentArgument, currentValue in arguments:
    if currentArgument in ("-v", "--verbose"):
        print ("enabling verbose mode")
    elif currentArgument in ("-h", "--help"):
        print ("displaying help")
    elif currentArgument in ("-s", "--start"):
        print(("will start range at (%s)") % (currentValue))
    elif currentArgument in ("-e", "--end"):
        print (("will end range at (%s)") % (currentValue))

for x in range(1, int(sys.argv[1]) + 1):
  if x % 2 == 0:
    if x % 3 == 0:
      print(f"{x} divisible by 2 and 3")
    else:
      print(f"{x} divisible by 2 and not by 3")
  elif x % 3 == 0:
    print(f"{x} divisible by 3 and not by 2")
  else:
    print(f"{x} not divisible by 2 or 3")