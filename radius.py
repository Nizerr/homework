from New_file import Point
from math import pi , trunc
class Radius:

    def __init__(self, radius, x=0, y=0):
        self.radius = radius
        self.point = Point(x,y)

    def __repr__(self):
        return f"Circle r={self.radius} with point {self.point}"

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return self.radius >= other.radius

    def __iadd__(self, other):
        return Radius(self.radius + other, self.point.x, self.point.y)

    def __len__(self):
        return self.__int__()

    def __int__(self):
        l = 2 * pi * self.radius
        return trunc(l)

    def __float__(self):
        return 2 * pi * self.radius



c1 = Radius(2, 0, 0)
c2 = Radius(2, 1, 1)
print(c1)
print(c2)
print(c1 == c2)
print(c1 != c2)
print(c1 >= c2)