from typing import Callable
from functools import wraps
def decorator(n: int):
    def new_decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("*"*n)
            func(*args, **kwargs)
            print("End")
        return wrapper()
    return new_decorator()
@decorator(5)
def f1(x):
    print(f"Call f1 = {x**2}")

f1(3)