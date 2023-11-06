from typing import List
from abc import ABC, abstractmethod

class Shope(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

class Circle(Shope):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r ** 2


def calculate_total_area(rects: List[Shope]):
    total_area = 0
    for obj in rects:
        total_area += obj.calculate_area()
    return total_area


r = Rectangle(5, 6)
s = Square(10)
#s.set(10, 1)
rects = [r, s]
print(calculate_total_area(rects))