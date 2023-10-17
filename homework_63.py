class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, target, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == target:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def delete_tail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_head(self):
        if self.head:
            self.head = self.head.next

    def delete_value(self, value, count):
        current = self.head
        prev = None
        deleted = 0
        while current:
            if current.data == value:
                if deleted < count:
                    if prev:
                        prev.next = current.next
                    else:
                        self.head = current.next
                    deleted += 1
                else:
                    break
            prev = current
            current = current.next

    def replace_value(self, old_value, new_vlue, replace_all=False):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_vlue
                if not replace_all:
                    break
            current = current.next

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("Кінець списку")

linked_list = LinkedList()
while True:
    print("\nМеню:")
    print("1. Додати елемент у хвіст списку")
    print("2. Додати елемент до списку на початок")
    print("3. Вставити новий елемент після певного значення")
    print("4. Видалити елемент з хвоста списку")
    print("5. Видалити елемент з голови списку")
    print("6. Видалити елемент із певним значенням")
    print("7. Замінити значення у списку")
    print("8. Визначити розмір списку")
    print("9. Показати вміст списку")
    print("0. Вийти")
    choice = input("Виберіть опцію: ")

    if choice == "1":
        data = input("Введіть дані для додавання в хвіст списку: ")
        linked_list.append(data)
    elif choice == "2":
        data = input("Введіть дані для додавання на початок списку: ")
        linked_list.prepend(data)
    elif choice == "3":
        target = input("Введіть значення, після якого потрібно вставити новий елемент: ")
        data = input("Введіть дані для вставки: ")
        linked_list.insert_after(target, data)
    elif choice == "4":
        linked_list.delete_tail()
    elif choice == "5":
        linked_list.delete_head()
    elif choice == "6":
        value = input("Введіть значення для видалення: ")
        count = int(input("Введіть кількість видалень: "))
        linked_list.delete_value(value, count)
    elif choice == "7":
        old_value = input("Введіть значення, яке потрібно замінити: ")
        new_value = input("Введіть нове значення: ")
        replace_all = input("Замінити всі входження? (так/ні): ").lower()
        replace_all = replace_all == "так"
        linked_list.replace_value(old_value, new_value, replace_all)
    elif choice == "8":
        print("Розмір списку:", linked_list.size())
    elif choice == "9":
        print("Вміст списку:")
        linked_list.display()
    elif choice == "0":
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")