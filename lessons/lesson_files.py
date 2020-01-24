import json

data = "This is some cats"

with open("./lesson-files.txt", "a") as file:
    print("Writing data to txt file...")
    try:
        file.write(f"{data}\n")
    except IOError as err:
        print(f"Error while writing to file: {err}", "\n")
    print("File written!\n")

with open("./lesson-files.txt", "r") as file:
    print("Reading from txt file...")
    try:
        data = file.readlines()
        for line in data:
            print(line)
    except IOError as err:
        print(f"Error while reading from file: {err}", "\n")
