class UserNameDescriptor:
    def __get__(self, instance, owner):
        return instance._username

    def __set__(self, instance, value):
        if not (4 <= len(value) <= 10):
            raise ValueError("Імя користувача повинне мати від 4 до 10 симвлоів")
        if not value[0].isalpha(): # Метод isalpha() повертає True, якщо всі символи є літерами алфавіту (a-z).
            raise ValueError("Імя користувача повинно починатися з літери")
        if not value.isalnum(): # Метод isalnum() повертає значення True, якщо всі символи є буквено-цифровими, що означають літери алфавіту (a-z) і цифри (0-9).
            raise ValueError("Імя користуача може містити тільки літери та цифри")
        instance._username = value

class Password:
    def __get__(self, instance, owner):
        return instance._password

    def __set__(self, instance, value):
        if len(value) < 8:
            return ValueError("Пароль має бути не менше 8 символів")
        instance._password = value

class User:
    username = UserNameDescriptor()
    password = Password()

    def __init__(self, username, password):
        self._username = username
        self._password = password


try:
    user_one = User("Jhon123", "123456789")
except ValueError as e:
    print(e)

try:
    user_two = User("Alan", "1234")
except ValueError as e:
    print(e)

user_three = User("jhondoe", "strongpass")
print(user_three.username)
print(user_three.password)