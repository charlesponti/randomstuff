
def print_args(old_function):
    """
    This function prints the args & kwargs of the
    decorated function. Used for Debugging.
    """
    def new_function(*args, **kwargs):
        print("args", args)
        print("kwargs", kwargs)
        return old_function(*args, **kwargs)

    return new_function