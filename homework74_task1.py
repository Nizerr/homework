class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class Category:
    def __init__(self, name):
        self.name = name
        self.subcategories = []
        self.products = []

    def add_subcategory(self, subcategory):
        self.subcategories.append(subcategory)

    def remove_subcategory(self, subcategory):
        if subcategory in self.subcategories:
            self.subcategories.remove(subcategory)

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_price(self):
        total_price = sum(product.get_price() for product in self.products)
        for subcategory in self.subcategories:
            total_price += subcategory.get_total_price()
        return total_price

class Store:
    def __init__(self):
        self.categories = []

    def create_category(self, category, parent_category=None):
        if parent_category is None:
            self.categories.append(category)
        else:
            parent_category.add_subcategory(category)

    def create_product(self, product, category):
        category.add_product(product)

    def get_total_price(self):
        total_price = 0
        for category in self.categories:
            total_price += category.get_total_price()
        return total_price

# Створюємо продукти
product1 = Product("Молоко", 42)
product2 = Product("Хліб", 32)
product3 = Product("Яйця", 6.5)

# Створюємо категорії
cat_food = Category("Продукти")
cat_dairy = Category("Молочні продукти")
cat_bakery = Category("Випічка")
cat_eggs = Category("Курячі яйця")

# Створюємо магазин
store = Store()

# Створюємо ієрархію категорій
store.create_category(cat_food)
store.create_category(cat_dairy, cat_food)
store.create_category(cat_bakery, cat_food)
store.create_category(cat_eggs, cat_food)

# Додаємо продукти до категорій
store.create_product(product1, cat_dairy)
store.create_product(product2, cat_bakery)
store.create_product(product3, cat_eggs)

# Виводимо перелік товарів та їх цін
def print_products(category, indent=0):
    for product in category.products:
        print("  " * indent + f"{product.name}: {product.get_price()} грн")
    for subcategory in category.subcategories:
        print("  " * indent + subcategory.name)
        print_products(subcategory, indent + 1)
    if indent > 0:
        print("-" * (indent * 2) + "-" * 20)

print("Перелік товарів та їх цін:")
print("-"* 20)
print_products(cat_food)

# Виводимо загальну ціну у магазині
total_price = store.get_total_price()
print(f"Загальна ціна у магазині: {total_price:.2f} грн")
