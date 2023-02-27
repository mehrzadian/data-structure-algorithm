from math import log2, pow
t = int(input())
ls = []
for i in range(t):
    m = int(input())
    line = list(map(int,input().split()))
    ls.append(line)



class Node:
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None

    


class Tree:
    def __init__(self, line):
        n = len(line)
        q = []
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

    

    def levelorder(self, root):
        x,q = [],[]
        q.append(root)
        while q:
            node = q.pop(0)
            if node.val == None:
                x.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
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
