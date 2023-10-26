class IShape:
    def get_area(self) -> float:
        pass

class Shape:
    def __init__(self, name: str):
        self.name = name

    def info(self):
        pass

class Square(Shape):
    def __init__(self, name: str, side:float):
        super().__init__(name)
        self.side = side

    def get_area(self) -> float:
        return self.side ** 2

class Circle(Shape):
    def __init__(self, name:str, radius:float):
        super().__init__(name)
        self.radius = radius

    def info(self):
        pass

    def get_area(self) -> float:
        return 3.14 * self.radius ** 2

class Pizza:
    def __init__(self, price: float, shape: IShape):
        self.price = price
        self.shape = shape

    def get_price(self) ->float:
        return self.price

    def get_shape_class(self) -> str:
        return type(self.shape).__name__

    def cut_pizza(self):
        pass


square = Square("Квадрат", 5.0)
circle = Circle("Коло", 3.0)
pizza = Pizza(10.0, square)

print(f"{square.name}, Площа: {square.get_area()}")
print(f"{circle.name}, Площа: {circle.get_area()}")
print(f"Піца, Ціна: {pizza.get_price()}, Форма: {pizza.get_shape_class()}")