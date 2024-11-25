class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            print("No instance exists. Creating a new one")

            cls.__instance = super(Logger, cls).__new__(cls)
            # place the instatntiation code here
        else:
            print("returning the previously creeated instance")

        return cls.__instance


# logger = Logger()
logger = Logger()
print(logger)
logger = Logger()
print(logger)
