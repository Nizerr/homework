class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end='-->')
            self.inorder_traversal(node.right)

    def search_in_subtree(self, node, value):
        if not node or node.key == value:
            return node
        left_search = self.search_in_subtree(node.left, value)
        if left_search:
            return left_search
        return self.search_in_subtree(node.right, value)

    def search(self, value):
        return self.search_in_subtree(self.root, value)


root = TreeNode('A')
root.left = TreeNode('B')
root.left.left = TreeNode('D')
root.left.left.left = TreeNode('H')
root.left.left.right = TreeNode('I')
root.left.right = TreeNode('E')
root.left.right.left = TreeNode('F')
root.left.right.right = TreeNode('K')
root.right = TreeNode('C')
root.right.left = TreeNode('G')

tree = Tree()
tree.root = root

print("Реалізація in-order")
tree.inorder_traversal(tree.root)

value_to_find = "F"

found_node = tree.search(value_to_find)
if found_node:
    print(f"\nЗнайдено вузол зі значенням {value_to_find}: {found_node.key}", end='')
else:
    print(f"Вузол зі значенням '{value_to_find}' не знайдено.")
