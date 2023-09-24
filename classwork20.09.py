class MyClass:
    rate = "123"

    def __init__(self, x, age=0):
        self.age = age
        self.x = x

    @staticmethod
    def get_tupe(n):
        result = MyClass.rate * n
        print(result)

    def get_tupe_2(self,n):
        result = type(self).rate * n
        print(result)

    @classmethod
    def get_tupe_3(cls, n, year):
        print(f"before create obj: {n} {year}")
        age = 2023 - year
        new_obj = cls(n, age)
        return new_obj

    @classmethod
    def make(cls, *args):
        print(f"Before create obj: {args}")
        cls.new_arre = "attr_class"
        new_obj = cls(*args)
        return new_obj


same_obj = MyClass.get_tupe_3(10, 2000)
print(MyClass.__dict__)




# MyClass.get_tupe_3(2)


# MyClass.get_tupe(3)
# obj.get_tupe_2(4)
# print(type(obj))
# print(MyClass.__dict__)
# print(MyClass.__module__)
# obj.__dict__["color"] = "black"
# print(obj.__dict__)
