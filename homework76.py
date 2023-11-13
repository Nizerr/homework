import json


# Клас для керування масивом рядків
class StringArrayManager:
    def __init__(self):
        self.string_array = []

    def load_from_keyboard(self):
        self.string_array = input("Введіть рядки (розділені комами): ").split(',')

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            self.string_array = file.read().splitlines()

    def check_element_type(self):
        # Перевіряємо, чи всі елементи є одного типу (рядки)
        return all(isinstance(s, str) for s in self.string_array)

    def sort(self, reverse=False):
        self.string_array.sort(reverse=reverse)

    def add_element(self, element):
        self.string_array.insert(0, element)

    def remove_element(self):
        if self.string_array:
            self.string_array.pop(0)

    def count_elements(self, value):
        # Знаходимо кількість елементів, які дорівнюють певному значенню
        return self.string_array.count(value)

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.string_array, file)

    def save_to_txt(self, filename):
        with open(filename, 'w') as file:
            file.write('\n'.join(self.string_array))


# Клас для роботи з числовим масивом
class NumericArrayManager(StringArrayManager):
    def __init__(self):
        super().__init__()

    def load_from_keyboard(self):
        self.string_array = input("Введіть числа (розділені комами): ").split(',')
        self.string_array = [float(x) for x in self.string_array]

    def calculate_average(self):
        # Знаходимо середнє значення числового масиву
        return sum(self.string_array) / len(self.string_array)


# Клас для реєстрації дій у лог-файлі
class LogManager:
    def log(self, message):
        with open("log.txt", "a") as file:
            file.write(message + "\n")


if __name__ == "__main__":
    array_manager = StringArrayManager()

    # Завантаження масиву з клавіатури
    array_manager.load_from_keyboard()

    # Завантаження масиву з файлу
    array_manager.load_from_file("data.txt")

    # Перевірка типу елементів
    if array_manager.check_element_type():
        print("Всі елементи є рядками.")
    else:
        print("Елементи різних типів.")

    # Сортування
    array_manager.sort()
    print("Сортування за зростанням:", array_manager.string_array)
    array_manager.sort(reverse=True)
    print("Сортування за спаданням:", array_manager.string_array)

    # Додавання та видалення елемента
    array_manager.add_element("Новий елемент")
    array_manager.remove_element()
    print("Після додавання та видалення:", array_manager.string_array)

    # Знаходження кількості елементів, які дорівнюють певному значенню
    count = array_manager.count_elements("Значення")
    print("Кількість 'Значення' у масиві:", count)

    # Збереження у JSON-файл
    array_manager.save_to_json("output.json")

    # Збереження у текстовий файл
    array_manager.save_to_txt("output.txt")

    # Робота з числовим масивом
    numeric_array_manager = NumericArrayManager()
    numeric_array_manager.load_from_keyboard()
    average = numeric_array_manager.calculate_average()
    print("Середнє значення числового масиву:", average)