class Person:

    def __new__(cls, name, age):
        print("Before magic method __new__")
        return super().__new__(cls)

    def __init__(self, name, age=0):
        print("begin init")
        self.age = age
        self.name = name

    @classmethod
    def make(cls, name, year):
        print(f"Before create obj: {name}, {year}")
        return cls(name, 2023 - year)


obj = Person("Jon", 20)
print(vars(obj))