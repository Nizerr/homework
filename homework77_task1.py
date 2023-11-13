class LoginRequired:
    def __init__(self, permission, permissions):
        self.permission = permission
        self.permissions = permissions

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.permission in self.permissions:
                return func(*args, **kwargs)
            else:
                raise ValueError(f"Немає доступа для користувача: {self.permission}")
        return wrapper

permissions = ["user", "admin"]

@LoginRequired(permission="user", permissions=permissions)
def data():
    print("secret data")

data()