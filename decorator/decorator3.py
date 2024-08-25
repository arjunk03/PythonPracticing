from functools import wraps


def logging(func):
    @wraps(func)
    def wrapper(name):
        """
        Doc for wrapper
        """
        print("calling the funcion")

        func(name)

        print("completed calling the function")

    return wrapper


@logging
def myFunc(name):
    """
    This is the doc we created
    """
    print(f"My name is {name}")


myFunc("arjun")
print(myFunc.__doc__)
