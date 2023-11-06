from abc import ABC, abstractmethod

class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class EatAble:
    def eat(self):
        print(f"eat ")

class Ostriche(Walkable):
    def walk(self):
        print("Ostriche is walking")

class Eagle(Walkable, Flyable):
    def fly(self):
        print("Eagle is flying")
    def walk(self):
        print("Eagle is walking")

try:
    obj = Eagle()
    obj.fly()
    obj.walk()
    obj2 = Ostriche()

    obj2.walk()

except Exception as e:
        # Print any exceptions that might occur
        print(e)