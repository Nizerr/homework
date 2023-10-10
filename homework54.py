import math
class Vector:
    def __init__(self, x, y, z):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float)):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise ValueError("Числа не вірні")

    def __str__(self):
        return f"Вектор ({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z

    def __rmul__(self, other):
        return self.__mul__(other)

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2))

    def __int__(self):
        return int(self.__len__())

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Невірний індекс")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value
        else:
            raise IndexError("Невірний індекс")

    def __contains__(self, item):
        return item in (self.x, self.y, self.z)

    def __bool__(self):
        return self.__len__() != 0

    def __call__(self):
        return Vector(self.x * 2, self.y * 2, self.z * 2)


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = Vector(1, 2, 3)

    print(v1)
    print(v1 == v2)
    print(v1 == v3)

    v4 = v1 + v2
    print(v4)

    v5 = v2 - v1
    print(v5)

    v1 += v2
    print(v1)

    v2 -= v3
    print(v2)

    scalar_product = v1 * v2
    print(scalar_product)

    scaled_vector = v1 * 2
    print(scaled_vector)

    length = len(v1)
    print(length)

    integer_length = int(v1)
    print(integer_length)

    neg_vector = -v1
    print(neg_vector)

    print(v1[0])
    print(v1[1])
    print(v1[2])

    v1[0] = 10
    v1[1] = 20
    v1[2] = 30
    print(v1)

    print(10 in v1)
    print(25 in v1)

    print(bool(v1))
    print(bool(Vector(0, 0, 0)))

    v6 = v1()
    print(v6)

