class Book:
    def __init__(self, title, author):
        self._attributes = {"title": title, "author": author}

    def __getattr__(self, name):
        print(f"Call __getattr__ {name}")
        if name in self._attributes:
            return self._attributes[name]
        else:
            raise AttributeError(f"Книга не має атрибуту {name}")

    def __setattr__(self, name, value):
        print(f"Call __setattr__ with {name=} {value=}")
        if name == "_attributes":
            super().__setattr__(name, value)
        else:
            self._attributes[name] = value

    def __delattr__(self, name):
        print(f"Call __delattr__ {name}")
        if name in self._attributes:
            del self._attributes[name]
        else:
            raise AttributeError(f"Книга не має атрибута {name}")

    def __getattribute__(self, name):
        print(f"Call __getattribute__ with {name}")
        if name in ("_attributes", "__dict__"):
            return super().__getattribute__(name)
        else:
            return super().__getattribute__("_attributes")[name]

print("1", "-" * 20)
book = Book("Python Programming", "Jhon Zelle")
print("2", "-" * 20)
book.year = 2016
print("3", "-" * 20)
print(book.__dict__)
print("4", "-" * 20)
print("book.year=", book.year)


