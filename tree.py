from BinaryTreePrinter import BinaryTreePrinter
from queue import Queue
from stack import Stack


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            nodes = Queue()
            nodes.enque(self.root)

            while True:
                checking_node = nodes.deque()
                if checking_node.left is None:
                    checking_node.left = TreeNode(val)
                    return
                elif checking_node.right is None:
                    checking_node.right = TreeNode(val)
                    return
                else:
                    nodes.enque(checking_node.left)
                    nodes.enque(checking_node.right)

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __insert_val(self, node, value):
        if node is None:
            return

        if node.val == value:
            return
        elif value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
                return
            self.__insert_val(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
                return
            self.__insert_val(node.right, value)

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.__insert_val(self.root, val)

    def __in_order(self, node):
        if node is None:
            return
        self.__in_order(node.left)
        print(node.val, end=" ")
        self.__in_order(node.right)

    def in_order(self):
        self.__in_order(self.root)

    def contains(self, val):
        nodes = Stack()
        nodes.push(self.root)

        while not nodes.is_empty():
            node = nodes.pop()
            print(f"checking node: {node.val}")
            if node.val == val:
                return True
            elif val < node.val:
                if node.left is not None:
                    nodes.push(node.left)
            else:
                if node.right is not None:
                    nodes.push(node.right)

        return False

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)


# my_tree = BinaryTree()
# for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
#     my_tree.insert(c)
# print(my_tree)

my_bst = BinarySearchTree()
for i in [10, 4, 54, 32, 45, 2, 5, 66, 78, 8, 53, 33, 6]:
    my_bst.insert(i)
    print(my_bst)

my_bst.in_order()
print()
print("contain 10: ", my_bst.contains(66))
print("contain 0: ", my_bst.contains(0))
