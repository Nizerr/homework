class Pesona:

    def __init__(self, name, age=0):
        self._name = name
        self.__age = age

    def __str__(self):
        return f"{self._name} {self.__age}"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


obj = Pesona("Jon", 20)
print(obj)
print(obj.age)
obj.age = 5
print(obj.age)
