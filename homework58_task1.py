class Size:
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self # Якщо спроба доступу до атрибута через клас, повертаємо сам дескриптор
        return len(obj.name) # Повертаємо довжину імені екземпляра Person

class Person:
    size_name = Size() # Створюємо екземпляр Size

    def __init__(self, name):
        self.name = name

person1 = Person("Jhon")
person2 = Person("Alice")

print(person1.size_name)
print(person2.size_name)