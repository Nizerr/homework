import re

class Descriptor:
    def __init__(self, var_name, min_lenght, max_lenght):
        self.var_name = var_name
        self.min_lenght = min_lenght
        self.max_lenght = max_lenght
        self.var = None

    def __get__(self, instance, owner):
        return self.var

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.var_name} має бути рядок")
        if not self.min_lenght <= len(value) <= self.max_lenght:
            raise ValueError(f"{self.var_name} довжина повинна бути між {self.min_lenght} та {self.max_lenght}")
        if self.var_name == "username" and not re.match(r'^[a-zA-Z][_a-zA-Z0-9-]*$', value):
            raise ValueError(f"Поганий {self.var_name} формат")
        if self.var_name == "first_name" and not re.match(r'^[a-zA-Z]', value):
            raise ValueError(f"Поганий {self.var_name} формат")
        if self.var_name == "last_name" and not re.match(r'^[a-zA-Z]+$', value):
            raise ValueError(f"Помилка {self.var_name} формату")
        if self.var_name == "password" and not re.match(r'^[a-zA-Z][_a-zA-Z0-9-]*$', value):
            raise ValueError(f"Помилка {self.var_name} формату")
        if self.var_name == "email" and not re.match(r'^[\w\.-]+@[\w\.-]+$', value):
            raise ValueError(f"Помилка {self.var_name} формату")
        self.var = value

class UniqueEmailDescriptor(Descriptor):
    def __set__(self, instance, value):
        if value in [user.email for user in instance._users]:
            raise ValueError(f"Email '{value}' вже зареїстрований")
        super().__set__(instance, value)

class User:
    _users = []

    username = Descriptor("username", 3, 16)
    first_name = Descriptor("first_name", 1, 20)
    last_name = Descriptor("last_name", 1, 20)
    password = Descriptor("password", 6, 16)
    email = UniqueEmailDescriptor("email", 6, 50)

    def __init__(self, username, first_name, last_name, password, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password= password
        self.email = email
        User._users.append(self)


if __name__ == "__main__":
    user1 = User("john_doe", "John", "Doe", "passw0rd", "john@example.com")
    user2 = User("alice_smith", "Alice", "Smith", "passw0rd", "alice@example.com")

    try:

        user3 = User("bob", "Bob", "Johnson", "passw0rd", "john@example.com")
    except ValueError as e:
        print(e)

    print(f"User 1 email: {user1.email}")
    print(f"User 2 email: {user2.email}")