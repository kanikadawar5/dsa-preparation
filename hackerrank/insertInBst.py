class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def __init__(self, counter) -> None:
        self.counter = counter
        pass

    def insert(self, root, val):
        if root is None:
            return Node(val)

        if val < root.data:
            self.counter += 1
            root.left = self.insert(root.left, val)
        else:
            self.counter += 1
            root.right = self.insert(root.right, val)
        return root

    def printNode(self, root):
        if root is None:
            return
        self.printNode(root.left)
        print(root.data)
        self.printNode(root.right)

    def printPreOrder(self, root):

        if root is None:
            return

        print(root.data)
        self.printNode(root.left)
        self.printNode(root.right)


def createBst(nums):
    root = Node(nums[0])
    i = 1
    sol = Solution(0)
    while i < len(nums):
        root = sol.insert(root, nums[i])
        print('Counter: ', sol.counter, ', num = ', nums[i])
        i += 1

    print('In order')
    sol.printNode(root)
    print('Pre Order')
    sol.printPreOrder(root)


print(createBst([7, 8, 1, 2, 3, 4, 5]))
