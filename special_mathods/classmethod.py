class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)

    def __repr__(self):
        return f"{type(self).__name__}({self.a}, {self.b} )"


a = A(1, 2)
print(repr(a))
b = A.from_sequence((20, 30))
print(repr(b))
