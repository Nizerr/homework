from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def fill_color(self, color):
        pass

    @abstractmethod
    def erase(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Малюю коло")

    def fill_color(self, color):
        print(f"Заповнюю коло колбором {color}")

    def erase(self):
        print("Видаляю коло")

class Rectangle(Shape):

    def draw(self):
        print("Малюю прямокутник")

    def fill_color(self, color):
        print(f"Заповнюю прямокутник кольором {color}")

    def erase(self):
        print("Видаляю прямокутник")

class Creator(ABC):
    @abstractmethod
    def create_product(self):
        pass

    def render(self, color):
        product = self.create_product()
        product.draw()
        product.fill_color(color)
        product.erase()

class CircleCreator(Creator):
    def create_product(self):
        return Circle()

class RectangleCreator(Creator):
    def create_product(self):
        return Rectangle()

if __name__ == "__main__":
    circle_creator = CircleCreator()
    circle_creator.render("червоний")

    rectangle_creator = RectangleCreator()
    rectangle_creator.render("синій")
