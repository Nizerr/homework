class HotDog:
    def __init__(self, name, price, ingredients, sauces=[]):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.sauces = sauces

class Order:
    def __init__(self):
        self.hotdogs = []
        self.total_price = 0
        self.payment_method = None

    def add_hotdog(self, hotdog):
        self.hotdogs.append(hotdog)
        self.total_price += hotdog.price

    def set_payment_method(self, method):
        self.payment_method = method

class Menu:
    def __init__(self):
        self.hotdogs = []

    def add_hotdog(self, hotdog):
        self.hotdogs.append(hotdog)

class DiscountCalculator:
    def discount(self, order):
        if len(order.hotdogs) >= 3:
            return order.total_price * 0.1
        else:
            return 0

class Sales:
    def __init__(self):
        self.sold_hotdogs = []
        self.total_revenue = 0

    def record_sale(self, order):
        self.sold_hotdogs.append(order)
        self.total_revenue += order.total_price

class Inventory:
    def __init__(self):
        self.ingredients = {}

    def add_ingredient(self, ingredient, quantity):
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity

class PaymentProcessor:
    def process_payment(self, order):
        if order.payment_method == 'cash':
            print(f'Оплата готівкою на суму {order.total_price} грн')
        elif order.payment_method == 'card':
            print('Оплата кредитною карткою здійснена')

class App:
    def __init__(self):
        self.menu = Menu()
        self.sales = Sales()
        self.inventory = Inventory()
        self.discount_calculator = DiscountCalculator()

    def display_menu(self):
        for i, hotdog in enumerate(self.menu.hotdogs):
            print(f"{i + 1}. {hotdog.name} - {hotdog.price} грн")

    def create_order(self):
        order = Order()
        while True:
            self.display_menu()
            choice = input("Виберіть номер хот-дога або 'q' для завершення замовлення: ")
            if choice == 'q':
                break
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.menu.hotdogs):
                    hotdog = self.menu.hotdogs[choice - 1]
                    order.add_hotdog(hotdog)
                    sauce_choice = input("Оберіть соус (1 - Кетчуп, 2 - Гірчиця, 3 - Сирний): ")
                    if sauce_choice == '1':
                        hotdog.ingredients.append("Кетчуп")
                    elif sauce_choice == '2':
                        hotdog.ingredients.append("Гірчиця")
                    elif sauce_choice == '3':
                        hotdog.ingredients.append("Сирний")
                    else:
                        print("Неправильний вибір соусу.")
                else:
                    print("Неправильний вибір хот-дога.")
            except ValueError:
                print("Неправильний вибір.")
        return order

    def process_order(self, order):
        discount = self.discount_calculator.discount(order)
        order.total_price -= discount
        print("Замовлення:")
        for hotdog in order.hotdogs:
            print(f'{hotdog.name} - {hotdog.price} грн')
        print(f'Загальна вартість: {order.total_price} грн')
        payment_method = input("Виберіть метод оплати ('cash' або 'card'): ")
        order.set_payment_method(payment_method)
        PaymentProcessor().process_payment(order)
        self.sales.record_sale(order)

    def display_sales_summary(self):
        print(f"Загальний прибуток: {self.sales.total_revenue} грн")
        print(f"Кількість проданих хот-догів: {len(self.sales.sold_hotdogs)}")

    def display_ingredients_inventory(self):
        print("Запаси інгредієнтів:")
        for ingredient, quantity in self.inventory.ingredients.items():
            print(f'{ingredient}: {quantity}')


if __name__ == "__main__":
    app = App()

    hotdog1 = HotDog("Стандартний хот-дог", 25, ["сосиска", "булочка"], ["Кетчуп"])
    hotdog2 = HotDog("Гострий хот-дог", 30, ["сосиска", "гірчиця", "халапеньйо"], ["Гірчиця", "Халапеньйо"])
    hotdog3 = HotDog("Дитячий хот-дог", 20, ["маленька сосиска", "маленька булочка"], ["Сирний"])

    app.menu.add_hotdog(hotdog1)
    app.menu.add_hotdog(hotdog2)
    app.menu.add_hotdog(hotdog3)

    app.inventory.add_ingredient("сосиска", 100)
    app.inventory.add_ingredient("булочка", 150)
    app.inventory.add_ingredient("кетчуп", 200)

    while True:
        print("\nГоловне меню:")
        print("1. Замовити хот-дог")
        print("2. Переглянути продажі")
        print("3. Переглянути запаси інгредієнтів")
        print("4. Вийти")
        choice = input("Оберіть опцію: ")
        if choice == '1':
            order = app.create_order()
            app.process_order(order)
        elif choice == '2':
            app.display_sales_summary()
        elif choice == '3':
            app.display_ingredients_inventory()
        elif choice == '4':
            break
        else:
            print("Неправильний вибір.")