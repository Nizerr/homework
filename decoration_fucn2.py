permissions = ["user", "admin"]

def required(permission):
    def decorate(func):
        def wrapper(*args,**kwargs):
            if permission in permissions:
                return func(*args, **kwargs)
            else:
                raise ValueError(f"Немає доступа для користувача: {permission}")
        return wrapper
    return decorate



@required(permission="jon")
def data():
    print("secret data")

data()