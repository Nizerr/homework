class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, max_size=-1):
        self.top = None
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.max_size != -1 and self.size == self.max_size

    def push(self, data):
        if not self.is_full():
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
            self.size += 1
            print(f"Pushed: {data}")
        else:
            print("Stack is full, Cannot push.")

    def pop(self):
        if not self.is_empty():
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            print(f"Popped: {data}")
        else:
            print("Stack is empty. Cannot pop")

    def size(self):
        return self.size

    def clear(self):
        self.top = None
        self.size = 0

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            return None


stack = Stack(max_size=5)

while True:
    print("\nМеню:")
    print("1. Додати рядок (push)")
    print("2. Виштовхнути рядок (pop)")
    print("3. Перевірити чи порожній стек")
    print("4. Перевірити чи повний стек")
    print("5. Розмір стеку")
    print("6. Повне очищення стеку")
    print("7. Отримати значення верхнього рядка (peek)")
    print("8. Вихід")

    choice = input("Оберіть операцію: ")

    if choice == "1":
        item = input("Введіть рядок для додавання: ")
        stack.push(item)
    elif choice == "2":
        stack.pop()
    elif choice == "3":
        if stack.is_empty():
            print("Стек порожній")
        else:
            print("Стек не порожній")
    elif choice == "4":
        if stack.is_full():
            print("Стек повний")
        else:
            print("Стек не повний")
    elif choice == "5":
        print(f"Розмір стеку: {stack.size}")
    elif choice == "6":
        stack.clear()
        print("Стек очищений")
    elif choice == "7":
        top_item = stack.peek()
        if top_item is not None:
            print(f"Значення верхнього рядка: {top_item}")
        else:
            print("Стек порожній")
    elif choice == "8":
        break







