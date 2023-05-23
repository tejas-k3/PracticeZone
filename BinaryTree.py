"""
A Binary tree is represented by a pointer to the topmost node (commonly known as the “root”) of the tree. If the tree is empty, then the value of the root is NULL. Each node of a Binary Tree contains the following parts:

Data
Pointer to left child
Pointer to right child

Basic Operation On Binary Tree:
Inserting an element.
Removing an element.
Searching for an element.
Traversing the tree.

Auxiliary Operation On Binary Tree:
Finding the height of the tree
Find the level of a node of the tree
Finding the size of the entire tree.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data, node):
        if self.root is None:
            self.root = Node(data)
        elif data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert(data, node.right)

    def delete(self, data):
        node = self.root
        if node is None:
            return node
        if data < node.data:
            node.left = self.delete(data, node.left)
        elif data > node.data:
            node.right = self.delete(data, node.right)
        else:
            # Case 1: Node has no child or only one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Case 2: Node has two children
            min_node = self._find_min(node.right)
            node.data = min_node.data
            node.right = self._delete_recursive(min_node.data, node.right)
        return node

    def search(self, data):
        node = self.root
        if node is None or node.data == data:
            return node

        if data < node.data:
            return self.search(data, node.left)
        else:
            return self.search(data, node.right)

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# Example usage
# tree = BinaryTree()
# tree.insert(50)
# tree.insert(30)
# tree.insert(20)
# tree.insert(40)
# tree.insert(70)
# tree.insert(60)
# tree.insert(80)

# # Search for a node
# result = tree.search(40)
# print("Search Result:", result.data if result else "Not Found")

# # Delete a node
# tree.delete(30)

# # Search again after deletion
# result = tree.search(30)
# print("Search Result:", result.data if result else "Not Found")
