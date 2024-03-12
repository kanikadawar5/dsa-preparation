import sys


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_next_node(node, min, max):

    if node is None:
        return True

    if node.data > max or node.data < min:
        return False

    return check_next_node(node.left, min, node.data) and check_next_node(node.right, node.data, max)


def check_binary_search_tree_(root):
    return check_next_node(root, sys.maxint, sys.minint)


n = node(1)
n.left
# 1 2 3 4 5 6 7
