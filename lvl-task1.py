from sys import getsizeof
#task 1
# class Count:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __getattr__(self, name):
#         print("Call __getattr__")
#         self.__dict__[name] = None
#         return None
#
#     def __getattribute__(self, item):
#         print(f"Call __getattr__ with {item=}")
#         if item == "version":
#             raise AttributeError("Доступ до атрибуту заборонено")
#         return object.__getattribute__(self, item)
#
#     def __setattr__(self, name, value):
#         print(f"Call __setattr__ with {name=} {value=}")
#         self.__dict__[name] = value
#
#
# obj = Count(1, 10)
# print(1, obj.start, obj.end)
# print()
# print(obj.__dict__)
# obj.version = "v-1.0"
# print(obj.__dict__)
# del obj.start
# print(obj.__dict__)

# task 2

# class Ten:
#     def __get__(self, instance, owner):
#         print(f"{instance} - {owner}")
#         return 10
#
#     def __set__(self, instance, value):
#         print(f"{self} - {instance} - {value}")
#         instance._test = value
# class A:
#     x = 5
#     y = Ten()
#
#
# a = A()
# print(a.x)
# a.y = 20
# print(a.__dict__)

#task 3
# class NameDescriptor:
#
#     def _init_(self, prefix="_", length=5):
#         self.prefix = prefix
#         self.length = length
#
#     def __get__(self, instance, owner):
#         return getattr (instance, self.var)
#
#     def _set__(self, instance, value):
#         if len(value) >= 5:
#             setattr(instance, self.var, value)
#         else:
#             raise ValueError
#     def __set_nane__(self, owner, name):
#         var_name = self.prefix + name
#         self.var = var_name
#
# class Users:
#     username = NameDescriptor ("__")
#     name = NameDescriptor()
#     Last_name = NameDescriptor()
#
#     def __init__ (self, username, name, last_name):
#         self.username = username
#         self.name = name
#         self.last_name = last_name
#
#
# U = Users("admin","Jon", "Smit")
# print (U.__dict__)
# # {' _username": "admin', "_name": "Jon'}

# class User:
#
#     __slots__ = ("username", "name", "last_name")
#     def __init__(self, username, name, last_name):
#         self.username = username
#         self.name = name
#         self.last_name = last_name
#
#
# U = User("admin", "Jon", "Smitt")
# print(U.username, U.name, U.last_name)
# size_u = getsizeof(U)
# print(size_u)

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data}, {self.next.data if self.next else None})"
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = node
#
#     def append_left(self, data, value):
#         right = self.head
#         left = self.head
#         node = Node(value)
#         while right:
#             if right.data == data:
#                 node.next = right
#                 if left:
#                     left.next = node
#                 else:
#                     self.head = node
#             left = right
#             right = right.next
#
#     def delete_first_node(self):
#         current = self.head
#         if current is None:
#             print("No data element to delete")
#         else:
#             self.head = current.next
#
#     def delete_last_node(self):
#         current = prev = self.head
#         while current:
#             if current.next is None:
#                 if current == self.head:
#                     self.head = None
#                 else:
#                     prev.next = None
#             prev = current
#             current = current.next
#
#     def iter(self):
#         current = self.head
#         while current:
#             print(current.data, end=" --> ")
#             current = current.next
#         print(": End")
#
#     def __len__(self):
#         count = 0
#         current = self.head
#         while current:
#             count += 1
#             current = current.next
#         return count
#
#     def search(self, data):
#         current = self.head
#         while current:
#             if current.data == data:
#                 return True
#             current = current.next
#         return False
#
#     def __contains__(self, data):
#         return self.search(data)
#
#     def __iter__(self):
#         self.current = self.head
#         return self
#
#     def __next__(self):
#         if self.current is not None:
#             data = self.current.data
#             self.current = self.current.next
#             return data
#         else:
#             raise StopIteration
#
# lst = LinkedList()
# lst.append(8)
# lst.append(6)
# lst.append(4)
# lst.append(2)
# lst.iter()
# print(lst.search(4), lst.search(5))
# print(4 in lst, 5 in lst)
# print("Довжина списку:", len(lst))
# print()
# lst.append_left(4, 5)
# lst.iter()
#
# for x in lst:
#     print(x, end=" ")

# class Node:
#
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data})"
#
# class Stack:
#
#     def __init__(self, max_size=-1):
#         self.head = None
#         self.max_size = max_size
#
#     def size(self):
#         return self.max_size
#
#     def push(self, data):
#         if self.max_size == 0:
#             raise Exception("Stack is empty")
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             node.next = self.head
#             self.head = node
#         self.max_size -=1
#
#     def pop(self):
#         if self.head is None:
#             raise Exception("Стек порожній")
#         else:
#             value = self.head.data
#             self.head = self.head.next
#             return value
#
#     def is_empty(self):
#         return self.head is None
#
#     def iter(self):
#         current = self.head
#         while current:
#             if current.next is None:
#                 print(current, end='')
#                 break
#             print(current, "->", end=" ")
#             current = current.next
#
#     def peek(self):
#         if self.is_empty():
#             raise Exception("Стак порожній")
#         else:
#             value = self.head.data
#             return value
#
#
#
#
# stack = Stack()
# stack.push(5)
# stack.iter()
# print()
# stack.push(6)
# stack.iter()
# print()
# stack.push(7)
# stack.iter()
# print(stack.pop())
# stack.iter()


# class Node:
#
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data})"
#
# class Queues:
#     def __init__(self):
#         self._head = None
#         self._tail = None
#         self._size = 0
#
#     def enqueue(self, data):
#         node = Node(data)
#         if self._size == 0:
#             self._head = self._tail = node
#         else:
#             self._tail.next = node
#             self._tail = node
#         self._size += 1
#
#     def dequeue(self):
#         if self._size == 0:
#             raise IndexError
#         node = self._head
#         self._head = node.next
#         self._size -= 1
#         if self._size == 0:
#             self._tail = None
#
#         return node.data
#
#
#     @property
#     def size(self):
#         return self._size
#
#     def iter(self):
#         current = self._head
#         while current:
#             if current.next is None:
#                 print(current, end='')
#                 break
#             print(current, "<-", end=" ")
#             current = current.next
#
#
# test1 = Queues()
# test1.enqueue(2)
# test1.enqueue(4)
# test1.enqueue(1)
# test1.enqueue(7)
# test1.iter()
# print()
# test1.dequeue()
# test1.iter()
# print()


# class Node:
#     def __init__(self, value, prev=None):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
#     def __repr__(self):
#         return str(self.value)
#
# class Tree:
#     def __init__(self, root: Node):
#         self.root = root
#
#     def preorder(self,start, trace):
#         if start:
#             trace = trace + str(start.value) + "--"
#             trace = self.preorder(start.left, trace)
#             trace = self.preorder(start.right, trace)
#         return trace
#
#     def postorder(self,start, trace):
#         if start:
#             trace = self.postorder(start.left, trace)
#             trace = self.postorder(start.right, trace)
#             trace = trace + str(start.value) + "--"
#         return trace
#
#     # def add_node(self, parent_value, new_node, new_node_value, type="left"):
#     #     parent_node = self.find_parent_by_value(node=self.root, parent_value)
#
#     def find_node_by_value(self, node, value):
#         if node is None:
#             return None
#         if node.value == value:
#             return node
#         left_result = self.find_node_by_value(node.left, value)
#         if left_result:
#             return left_result
#         return self.find_node_by_value(node.right, value)
#
#
#
#
# root = Node(1)
# tree = Tree(root)
#
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.right = Node(6)
# print(tree.preorder(tree.root, trace=""))
#
# search_node = tree.find_node_by_value(tree.root, 6)
# if search_node:
#     print(search_node.value)




