class A:
    def __init__(self):
        pass

    @staticmethod
    def from_sequence(name):
        return "The name is ", name

    def __repr__(self):
        return f"{type(self).__name__}({self.a}, {self.b} )"


a = A()
print(a.from_sequence("test"))
print(A.from_sequence("data"))
