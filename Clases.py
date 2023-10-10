def get_count(self):
    print("Call method get_count")
    return self.count

MyClass = type("MyClass", (), {"username": "admin", "count": 0,"info": get_count})

obj = MyClass()
print(type(obj))
print(obj.username)
obj.info()