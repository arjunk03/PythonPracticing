import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        pass

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    def calculate_area(self):
        return self._radius**2 * math.pi


circle = Circle(100)
print(circle.radius)
