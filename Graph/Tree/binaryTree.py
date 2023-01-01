class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class binaryTree:
    def __init__(self, root):
        self.root = root

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.data, end=" ")
            self.inorderTraversal(root.right)

    def preorderTraversal(self, root):
        if root:
            print(root.data, end=" ")
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

    def postorderTraversal(self, root):
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            print(root.data, end=" ")

    def levelorderTraversal(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while (len(queue) > 0):
            print(queue[0].data)
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        queue = []
        queue.append(self.root)
        while (len(queue)):
            node = queue.pop(0)
            print("node : ", node)
            if node.left is not None:
                print("node left not none")
                queue.append(node.left)
            else:
                print("node left is NONE")
                node.left = Node(data)
                return
            if node.right is not None:
                print("node right not none")
                queue.append(node.right)
            else:
                print("node left is NONE")
                node.right = Node(data)
                return

    def delete(self, data):
        ''' 
        find te deepest element, replace it with the element that has the data
        '''
        if self.root is None:
            return
        queue = []
        nodeToDelete = None
        queue.append(self.root)
        while (len(queue)):
            node = queue.pop(0)
            last = node  # the most downward right node
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        queue.append(self.root)
        while (len(queue)):
            node = queue.pop(0)
            if node.data == data:
                node.data = last.data
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node.right is last:
                node.right = None
            if node.left is last:
                node.left = None
        return

    def height(self, root):
        if root is None:
            return 0
        return max(binaryTree.height(root.left) , binaryTree.height(root.right) )+1


root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)
root.right.right.right= Node(52)
binaryTree = binaryTree(root)

#     10
#    /  \
#  11     9
#   /   /  \
# 7   15    8

print("preorder traversal before insertion:",)
print(binaryTree.preorderTraversal(root))

key = 12
binaryTree.insert(key)

print()
print("Inorder traversal after insertion:")
binaryTree.inorderTraversal(root)
print()
print(binaryTree.height(root))
