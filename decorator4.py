from functools import wraps


def select_logging(logger_name):
    def logging(func):
        @wraps(func)
        def csv(name):
            """
            Doc for wrapper
            """
            print("calling the funcion csv ")

            func(name)

            print("completed calling the function csv ")

        @wraps(func)
        def xlsx(name):
            """
            Doc for wrapper
            """
            print("calling the funcion xlsx")

            func(name)

            print("completed calling the function xlsx")

        if logger_name == "csv":
            return csv
        else:
            return xlsx

    return logging


@select_logging("xlx")
def myFunc(name):
    """
    This is the doc we created
    """
    print(f"My name is {name}")


myFunc("arjun")
print(myFunc.__doc__)
