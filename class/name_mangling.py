#!/usr/bin/env python
class Sample:
    def __init__(self, value):
        self.__value = value

    def __method(self):
        print("values is ", self.__value)


sample = Sample(5)
print(vars(sample))
print(dir(sample))
print(vars(Sample))

print(sample._Sample__value)
print(sample._Sample__method())
