import math

class Circle:

    def __init__(self, radius=1):
        self.radius = radius


    def __str__(self):
        return f"Коло з радіусом {self.radius}"

    def area(self):
        return math.pi * self.radius ** 2

    def ference(self):
        return 2 * math.pi * self.radius

circle1 = Circle(2)
circle2 = Circle(3)

print(circle1)
print(circle2)

# Площа першого кола
area1 = circle1.area()
print(f"Площа першого кола: {area1:.2f}")

# Довжина другого кругу
ference1 = circle2.ference()
print(f"Довжина другого круга: {ference1:.2f}")