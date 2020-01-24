import getopt, sys


def get_args_with_getopt():
    # Get list of arguments passed to Python command
    fullCmdArguments = sys.argv[1:]

    for idx, arg in enumerate(fullCmdArguments):
        if arg[0] != "-":
            fullCmdArguments[idx] = None
        if arg[0] == "-":
            break

    args = [arg for arg in fullCmdArguments if arg != None]

    unixOptions = "h:v:s:e:"
    gnuOptions = ["help", "verbose", "start", "end"]

    try:
        options, arguments = getopt.getopt(args, unixOptions, gnuOptions)
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    return options, arguments


options, arguments = get_args_with_getopt()

start = 1  # Default start of range to
end = 1

for opt, arg in options:
    if opt in ("-v", "--verbose"):
        print("enabling verbose mode")
    elif opt in ("-h", "--help"):
        print("displaying help")
    elif opt in ("-s", "--start"):
        start = int(arg)
    elif opt in ("-e", "--end"):
        end = int(arg)

for x in range(start, int(end) + 1):
    if x % 2 == 0:
        if x % 3 == 0:
            print(f"{x} divisible by 2 and 3")
        else:
            print(f"{x} divisible by 2 and not by 3")
    elif x % 3 == 0:
        print(f"{x} divisible by 3 and not by 2")
    else:
        print(f"{x} not divisible by 2 or 3")
