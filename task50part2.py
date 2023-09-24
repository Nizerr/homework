class Car:
    count = 0

    def __init__(self, model, year, manufactured, engine_size, color, price):
        self.model = model
        self.year = year
        self.manufactured = manufactured
        self.engine_size = engine_size
        self.color = color
        self.price = price
        Car.count += 1

    def __str__(self):
        return f"{self.year} {self.manufactured} {self.model} {self.color} {self.price}"

    def new_color(self, new_color):
        self.color = new_color

    def new_price(self, new_price):
        self.price = new_price

    # Методи класу пов'язані з класом, а не з конкретними об'єктами класу.
    # Основна відмінність між методом класу і звичайним методом класу полягає в тому, що метод класу
    # приймає перший аргумент, який зазвичай називається < cls >,
    # і цей аргумент вказує на сам клас, а не на конкретний об'єкт.
    # Пояснення що таке ->@classmethod

    @classmethod
    def get_count(cls):
        return cls.count

car1 = Car("Civic", 2022, "Honda", "2.0L", "Сірий", 25000)
car2 = Car("Accord", 2023, "Honda", "2.5L", "Чорний", 30000)

print(car1)
print(car2)

car1.new_color("Жовтий")
car2.new_price(32000)

print(f"Ваш автомобіль {car1.manufactured} {car1.model} має новий колір: {car1.color}")
print(f"Автомобіль {car2.manufactured} {car2.model} має оновлену ціну: {car2.price}")

count_cars = Car.get_count()
print(f"Загальна кількість автомобілів в каталозі: {count_cars}")
