from ABRNode import *


class ABR:

    def __init__(self):
        self.root = None

    def setRoot(self, key):
        self.root = ABRNode(key)

    def insert(self, key):
        if self.root is None:
            self.setRoot(key)
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentNode, key):
        if key <= currentNode.key:
            if currentNode.left:
                self.insertNode(currentNode.left, key)
            else:
                currentNode.left = ABRNode(key)
        elif key > currentNode.key:
            if currentNode.right:
                self.insertNode(currentNode.right, key)
            else:
                currentNode.right = ABRNode(key)

    def treeSearch(self, x, key):
        if x is None or key == x.key:
            return x
        if key < x.key:
            return self.treeSearch(x.left, key)
        else:
            return self.treeSearch(x.right, key)

    def inOrder(self, x):
        if x is not None:
            self.inOrder(x.left)
            # print(x.key)
            self.inOrder(x.right)


