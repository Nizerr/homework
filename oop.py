class Person:
    """
    Клас відповідає за поповненя рахунока персони
    """
    def __init__(self, name='Rostyslav', money=0):
        self.name = name
        self.money = money
        self.known_people = []  # Додайте атрибут для списку знайомих
        print('A new Person is born =', self.name)

    def __str__(self):
        return self.name + str(self.money)

    def giveMoney(self, delta):
        self.money += delta
        print(f'Рахунок {self.name} поповннено на суму {delta:.2f}, всього {self.money:.2f}')

    def know(self, person):
        """
        Додає іншу людину до списку знайомих.
        """
        self.known_people.append(person)

    def is_known(self, person):
        """
        Перевіряє, чи знайомі дві людини.
        """
        return person in self.known_people

a = Person()
b = Person()
c = Person('Petro', 10)
d = Person('Ira', 30)
print('A: Name = {}, money = {:.2f}'.format(a.name, a.money))
print('B: Name = {}, money = {:.2f}'.format(b.name, b.money))

a.name = 'Ivan'
b.name = 'Anna'
b.money = 100.2852

b.giveMoney(40)
a.giveMoney(50.127)

# Додамо знайомих
a.know(b)
b.know(c)
c.know(d)

# Перевірка, чи знайомі
print(f"{a.name} knows {b.name}: {a.is_known(b)}")
print(f"{a.name} knows {c.name}: {a.is_known(c)}")

print('A: Name = {}, money = {:.2f}'.format(a.name, a.money))
print('B: Name = {}, money = {:.2f}'.format(b.name, b.money))

