class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        # yield (self.a, self.b)
        yield from (self.a, self.b)


print(list(A(1, 2)))
