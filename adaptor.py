from math import sqrt


class RoundPeg:
    def __init__(self, radius: int):
        self._radius = radius

    def get_radius(self):
        return self._radius

class SquarePeg:
    def __init__(self, width: int):
        self._width = width

    def get_width(self):
        return self._width

class SquarePegAdapter(RoundPeg):
    def __init__(self, peg: SquarePeg):
        self._peg = peg

    def get_radius(self):
        return self._peg.get_width() * sqrt(2) / 2


class RoundHole:
    def __init__(self, radius: int):
        self._radius = radius

    def fits(self, peg: RoundPeg):
        result = self.get_radius() >= peg.get_radius()
        print(f"Fit: {result}")
        return result

    def get_radius(self):
        return self._radius


hole = RoundHole(5)
rpeg = RoundPeg(4)
hole.fits(rpeg)
print()
small_sqpeq = SquarePeg(5)
large_sqpeq = SquarePeg(10)

small_sqpeq_adapter = SquarePegAdapter(small_sqpeq)
large_sqpeq_adapter = SquarePegAdapter(large_sqpeq)

hole.fits(small_sqpeq_adapter)
hole.fits(large_sqpeq_adapter)



