from functools import wraps
from datetime import datetime

def log_call(file):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            # Отримуємо поточний час
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Відкриваємо файл у режимі додавання
            with open(file, 'a') as log_file:
                # Записуємо інформацію про виклик методу у файл
                log_file.write(f"{current_time} - Method {func.__name__} called\n")

            result = func(self, *args, **kwargs)

            return result

        return wrapper
    return decorator

class MyClass:
    @log_call(file="test.log")
    def info(self):
        print("This is my method")

my_instance = MyClass()

my_instance.info()