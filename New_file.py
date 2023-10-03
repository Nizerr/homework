class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} {self.y}"

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __add__(self, other):
        if isinstance(other, Point):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return (new_x, new_y)
        elif isinstance(other, (int, float)):
            new_x = self.x + other
            new_y = self.y = other
            return Point(new_x, new_y)
        else:
            raise TypeError("Error operand")

    def __radd__(self, other):
        return self.__add__(other)

    def __len__(self):
        abs(self.x) + abs(self.y)


a = Point(2, 3)
b = Point(2, 3)
print(a)
print(b)
print(id(a), id(b))
print(a == b)
c = a + b
print(c, type(c))