import getopt, sys

def get_arguments():
  # Get list of arguments passed to Python command
  fullCmdArguments = sys.argv

  # Return only arguments with name of Python file
  return fullCmdArguments[1:]

def get_args_with_getopt():
  unixOptions = ["hH:sS:v"]
  gnuOptions = ["help", "start=", "end=", "verbose"]

  try:
    options, arguments = getopt.getopt(get_arguments(), unixOptions, gnuOptions)
  except getopt.error as err:
    print(str(err))
    sys.exit(2)

  return options, arguments

options, arguments = get_args_with_getopt()
print(options, arguments)
for currentArgument in arguments:
    if currentArgument in ("-v", "--verbose"):
        print ("enabling verbose mode")
    elif currentArgument in ("-h", "--help"):
        print ("displaying help")
    # elif currentArgument in ("-s", "--start"):
        # print(("will start range at (%s)") % (currentValue))
    # elif currentArgument in ("-e", "--end"):
        # print (("will end range at (%s)") % (currentValue))

# for x in range(1, int(sys.argv[1]) + 1):
#   if x % 2 == 0:
#     if x % 3 == 0:
#       print(f"{x} divisible by 2 and 3")
#     else:
#       print(f"{x} divisible by 2 and not by 3")
#   elif x % 3 == 0:
#     print(f"{x} divisible by 3 and not by 2")
#   else:
#     print(f"{x} not divisible by 2 or 3")