# from math import sin, pi
# class Derivate:
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self, x):
#         dx = 1e-5
#         result = (self._func(x + dx) - self._func(x))/dx
#         return result
#
# @Derivate
# def my_sin(x):
#     return sin(x)
#
#
# print(my_sin(pi/2))


def my_decorated(func):
    def wrapper(self):
        print("*"*10)
        func(self)
        print("*"*10)
    return wrapper

class Test:
    def __init__(self, name):
        self.name = name

    @my_decorated
    def info(self):
        print(f"info {self.name}")

t = Test("init")
t.info()