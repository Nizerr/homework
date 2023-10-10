from sys import getsizeof
#task 1
# class Count:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __getattr__(self, name):
#         print("Call __getattr__")
#         self.__dict__[name] = None
#         return None
#
#     def __getattribute__(self, item):
#         print(f"Call __getattr__ with {item=}")
#         if item == "version":
#             raise AttributeError("Доступ до атрибуту заборонено")
#         return object.__getattribute__(self, item)
#
#     def __setattr__(self, name, value):
#         print(f"Call __setattr__ with {name=} {value=}")
#         self.__dict__[name] = value
#
#
# obj = Count(1, 10)
# print(1, obj.start, obj.end)
# print()
# print(obj.__dict__)
# obj.version = "v-1.0"
# print(obj.__dict__)
# del obj.start
# print(obj.__dict__)

# task 2

# class Ten:
#     def __get__(self, instance, owner):
#         print(f"{instance} - {owner}")
#         return 10
#
#     def __set__(self, instance, value):
#         print(f"{self} - {instance} - {value}")
#         instance._test = value
# class A:
#     x = 5
#     y = Ten()
#
#
# a = A()
# print(a.x)
# a.y = 20
# print(a.__dict__)

#task 3
# class NameDescriptor:
#
#     def _init_(self, prefix="_", length=5):
#         self.prefix = prefix
#         self.length = length
#
#     def __get__(self, instance, owner):
#         return getattr (instance, self.var)
#
#     def _set__(self, instance, value):
#         if len(value) >= 5:
#             setattr(instance, self.var, value)
#         else:
#             raise ValueError
#     def __set_nane__(self, owner, name):
#         var_name = self.prefix + name
#         self.var = var_name
#
# class Users:
#     username = NameDescriptor ("__")
#     name = NameDescriptor()
#     Last_name = NameDescriptor()
#
#     def __init__ (self, username, name, last_name):
#         self.username = username
#         self.name = name
#         self.last_name = last_name
#
#
# U = Users("admin","Jon", "Smit")
# print (U.__dict__)
# # {' _username": "admin', "_name": "Jon'}

class User:

    __slots__ = ("username", "name", "last_name")
    def __init__(self, username, name, last_name):
        self.username = username
        self.name = name
        self.last_name = last_name


U = User("admin", "Jon", "Smitt")
print(U.username, U.name, U.last_name)
size_u = getsizeof(U)
print(size_u)