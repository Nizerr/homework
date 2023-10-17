class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_head(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_tail(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_by_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current == self.head:
                    self.delete_head()
                elif current == self.tail:
                    self.delete_tail()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

    def insert_at_index(self, data, index):
        if index < 0:
            raise IndexError("Невірний індекс")
        if index == 0:
            self.append_head(data)
            return
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Індеск за діапазоном")
            current = current.next
        new_node = Node(data)
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end='<->')
            current = current.next
        print("End")

    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end='<->')
            current = current.prev
        print("End")

    def clear(self):
        self.head = self.tail = None


test1 = DoublyLinkedList()
test1.append_head(1)
test1.append_head(2)
test1.append_tail(3)
test1.append_tail(4)
test1.traverse_forward()
test1.traverse_backward()

test1.delete_head()
test1.delete_tail()
test1.delete_by_value(3)
test1.traverse_forward()

test1.insert_at_index(5, 0)
test1.insert_at_index(6, 1)
test1.traverse_forward()

test1.clear()
#test1.traverse_forward()