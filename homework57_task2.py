class Dynamic:
    def __init__(self):
        self.__attributes = {}

    def __setattr__(self, name, value):
        if name == "__attributes":
            super().__setattr__(name, value)
        else:
            self.__attributes[name] = value

    def __delattr__(self, name):
        if name == "__attributes":
            raise AttributeError("Неможливо видалити атрибут __attributes")
        elif name in self.__attributes:
            del self.__attributes[name]
        else:
            raise AttributeError(f"Динамічний об'єкт не має атрибута {name}")

    def __getattribute__(self, name):
        if name == "_Dynamic__attributes":
            raise AttributeError("Доступ до атрибута __attributes заборонено")
        elif name in super().__getattribute__("_Dynamic__attributes"):
            return super().__getattribute__("_Dynamic__attributes")[name]
        else:
            return super().__getattribute__(name)

dynamic_obj = Dynamic()
dynamic_obj._Dynamic__attributes["name"] = "John Doe"

print(dynamic_obj.__dict__)
print(dynamic_obj.name)

del dynamic_obj.name

print(dynamic_obj.__dict__)
print(hasattr(dynamic_obj, "name"))



