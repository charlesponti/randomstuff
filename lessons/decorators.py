"""
This file shows how to define and use a function decorator
"""


def transaction_closure(fn):
    def wrapper(value, **kwargs):
        if not value:
            raise Exception(f"{value} is not truthy")
        return fn(value, **kwargs)

    return wrapper


@transaction_closure
def some_function(value):
    print(f"{value} is truthy")


some_function("Whattttt")
some_function(15)
some_function(True)


def multiplier(multiplier):
    def multiplier_generator(old_function):
        def new_function(*args, **kwargs):
            if kwargs.get("foo") == 1:
                print("You sent a keyword of 1")
            return old_function(args[0] * multiplier)

        return new_function

    return multiplier_generator


@multiplier(3)
def multiply_by_three(answer):
    return answer


print(multiply_by_three(5, foo=1))
