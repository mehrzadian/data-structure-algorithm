from math import log2, pow
t = int(input())
ls = []
for i in range(t):
    m = int(input())
    line = input().split()
    ls.append(line)
# print(ls)


class Node:
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None

    # def smallestChild(self, node):
    #     if node.left == None and node.right == None:
    #         return
    #     return node.left

    # def largestChild(self, node):
    #     if node.left == None and node.right == None:
    #         return
    #     return node.right

    # def displace(self):
    #     x = self.smallestChild(self)
    #     y = self.largestChild(self)
    #     if y.val - x.val == -1:
    #         self.right, self.left = self.left, self.right
    #         return 1
    #     elif y.val - x.val < -1:
    #         return False
    #     elif y.val - x.val > 1:
    #         return False
    #     return True


class Tree:
    def __init__(self, line):
        n = len(line)
        q = []
        line = [int(i) for i in line]
        # line=line[::-1]
        # print(line)
        self.root = Node()
        q.append(self.root)
        for i in range(int(log2(n))+1):
            p = int(pow(2, i))
            if p == n:
                for j in range(p):
                    node = q.pop(0)
                    node.val = line.pop(0)
            else:
                for j in range(p):
                    node = q.pop(0)
                    node.left = Node()
                    node.right = Node()
                    q.append(node.left)
                    q.append(node.right)

    # def inorder(self, root):
    #     if root:
    #         self.inorder(root.left)
    #         print(root.val)
    #         self.inorder(root.right)

    # def preorder(self, root):
    #     if root:
    #         print(root.val)
    #         self.preorder(root.left)
    #         self.preorder(root.right)

    # def postorder(self, root, q=[]):
    #     if root:
    #         self.postorder(root.left, q)
    #         self.postorder(root.right, q)

    #         q.append(root)

    #     q = [i for i in q if i.val == None]
    #     return q

    def levelorder(self, root):
        x = []
        q = []
        q.append(root)
        while q:
            node = q.pop(0)
            x.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        x = [i for i in x if i.val == None]
        x = x[::-1]
        return x

    def deliciousTree(self, root, lenItem):
        q = self.levelorder(root)
        if len(q) == 0 and root.val == 1:
            return 0
        elif len(q) == 0 and root.val != 1:
            return -1

        number = 0
        node = q.pop(0)
        level = 0
        currentlevel = lenItem//2
        while q:

            if currentlevel == 0:
                level += 1
                currentlevel = lenItem//2

            if node.left.left is None:

                if node.left.val-node.right.val == 1:

                    number += 1
                    node.left, node.right = node.right, node.left

                elif (node.left.val-node.right.val > 1) or (node.left.val-node.right.val < -1):

                    return -1
                node.val = node.left.val
            else:

                if node.left.val > node.right.val:
                    number += 1
                    node.left, node.right = node.right, node.left

                elif node.right.val - node.left.val > pow(2, level):

                    return -1
                node.val = node.left.val
            currentlevel -= 1

            node = q.pop(0)

        if root.right.val < root.left.val:
            number += 1
            node.left, node.right = node.right, node.left

        return number


for item in ls:
    
    
    t = Tree(item)
    print(t.deliciousTree(t.root, len(item)))
    # t.inorder(t.root)
