def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 11  # very friendly, decrease age even more :-)
        method_to_decorate(self, lie)

    return wrapper


class Lucy(object):
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("I am {0}, what did you think?".format(self.age + lie))


l = Lucy()
l.sayYourAge(-3)
