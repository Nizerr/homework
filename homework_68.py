from abc import ABC, abstractmethod

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree(ABC):
    def __init__(self, root=None):
        self.root = root

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def remove(self, value):
        pass

    @abstractmethod
    def find_min(self):
        pass

    @abstractmethod
    def search(self, value):
        pass

class MyBinarySearchTree(BinarySearchTree):
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.key:
            node.left = self._insert(node.left, value)
        elif value > node.key:
            node.right = self._insert(node.right, value)
        return node

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if node is None:
            return node
        if value < node.key:
            node.left = self._remove(node.left, value)
        elif value > node.key:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.key = self.find_min_value(node.right)
            node.right = self._remove(node.right, node.key)
        return node

    def find_min(self):
        if self.root is None:
            return None
        return self.find_min_value(self.root)

    def find_min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.key == value:
            return node
        if value < node.key:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


values = [12, 19, 8, 4, 10, 5, 21, 11, 15, 9, 1, 14, 16]
bs = MyBinarySearchTree()
for value in values:
    bs.insert(value)

inorder_result = bs.inorder()
print("In-order traversal:", inorder_result)

search_value = 15
result = bs.search(search_value)
if result:
    print(f"Знайдено вузол зі значенням {search_value}.")
else:
    print(f"Вузол зі значенням {search_value} не знайдено.")

min_value = bs.find_min()
print("Мінімальне значення", min_value)

node_remove = [11, 10, 12]
for value in node_remove:
    bs.remove(value)
    print(f"Вузол зі значенням {value} видалено.")
    inorder_result = bs.inorder()
    print("In-order traversal:", inorder_result)