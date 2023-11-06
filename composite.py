from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def execute(self) -> float:
        pass

class Product(Component):
    def __init__(self, name, cost):
        self._name = name
        self._cost = cost

    def execute(self) -> float:
        return self._cost

class Box(Component):
    def __init__(self, name):
        self._name = name
        self._product = []

    def add(self, c: Component):
        self._product.append(c)

    def remove(self, c: Component):
        self._product.remove(c)

    def execute(self) -> float:
        cost = 0
        for children in self._product:
            cost_children = children.execute()
            cost += cost_children
        return cost


box_1 = Box("Box-1")
box_2 = Box("Box-2")
box_3 = Box("Box-3")
product_1 = Product("Lg smart",  200)
product_2 = Product('Samsung QlED 1980p', 400)
product_3 = Product("IPhon 15", 100)
product_4 = Product("Nokia 3310", 223)

box_1.add(product_1)
box_1.add(box_2)
box_2.add(product_2)
box_2.add(product_3)
box_2.add(box_3)
box_3.add(product_4)

print(box_1.execute())
