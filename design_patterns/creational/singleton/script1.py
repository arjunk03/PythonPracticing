class Logger:
    __instance = None

    def __init__(self):
        raise RuntimeError("Call get_instane() instead")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            print("No instance exists. Creating a new one")

            cls.__instance = cls.__new__(cls)
        else:
            print("returning the previously creeated instance")

        return cls.__instance


# logger = Logger()
logger = Logger.get_instance()
print(logger)
logger = Logger.get_instance()
print(logger)
