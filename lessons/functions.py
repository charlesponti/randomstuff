#
# Example file for working with functions
#

# define a basic function
def function1():
    print("I am a function")


# function1()
# print(function1())
# print(function1)


# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)


# function that returns a value
def cube(x):
    return x * x * x


# function with default value for an argument
def power(arg1, arg2=2):
    current = 1
    for _ in range(arg2):
        current = current * arg1

    print(f"{arg1} to the power of {arg2} is {current}")


power(3)
power(3, 4)

# function with variable number of arguments
