from RBNode import *


class RB:

    def __init__(self):
        self.nil = RBNode(None, None)
        self.root = self.nil

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def insert(self, key):
        z = RBNode(key, self.nil)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = "R"
        self.rbInsertFixUp(z)

    def rbInsertFixUp(self, z):
        while z.p.color == "R":
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == "R":
                    z.p.color = "B"
                    y.color = "B"
                    z.p.p.color = "R"
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.leftRotate(z)
                    z.p.color = "B"
                    z.p.p.color = "R"
                    self.rightRotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == "R":
                    z.p.color = "B"
                    y.color = "B"
                    z.p.p.color = "R"
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.rightRotate(z)
                    z.p.color = "B"
                    z.p.p.color = "R"
                    self.leftRotate(z.p.p)
        self.root.color = "B"

    def inOrder(self, x):
        if x != self.nil:
            self.inOrder(x.left)
            # print(x.key)
            self.inOrder(x.right)

    def treeSearch(self, x, key):
        if x == self.nil or key == x.key:
            return x
        if key < x.key:
            return self.treeSearch(x.left, key)
        else:
            return self.treeSearch(x.right, key)
