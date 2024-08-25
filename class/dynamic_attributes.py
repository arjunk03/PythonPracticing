class Sample:
    """
    sample class
    """

    pass


sample = Sample()
print(sample.__doc__)
print(vars(sample))

setattr(sample, "name", "arjun")
print(vars(sample))
print(getattr(sample, "name"))
print(sample.__dict__)


def __init__(self, name):
    self.name = name


sample.__init__ = __init__
print(vars(sample))
