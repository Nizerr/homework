class Rectangle:
    name = "Rectangle-are"

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"Rectangle: {self.length} x {self.width}"

    def area(self):
        return self.length * self.width

    def info(self):
        print(f"Info: {self.length} x {self.width} = {self.area()}")

    def change_atr(self):
        new_lenght = int(input("Enter new lenght: "))
        new_width = int(input("Enter new width: "))
        self.length = new_lenght
        self.width = new_width
        print("Змінено атрибути об'єкта успішно!")


if __name__ == '__main__':
    obj = Rectangle(3, 5)
    print(obj)
    obj.info()
    obj.change_atr()
    obj.info()