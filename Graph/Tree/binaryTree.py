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
            print( root.data, end=" ")
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
    def lastElement(self, root):
        '''the most downward right element'''
        queue = []
        queue.append(self.root)
        while (len(queue)):
            node = queue.pop(0)
            last = node  # the most downward right node
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return last
    def delete(self, data):
        ''' 
        find te deepest element, replace it with the element that has the data
        '''
        if self.root is None:
            return
        queue = []
        nodeToDelete = None
        last = binaryTree.lastElement(self.root)
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
        
    def search(self, root, data):
        return None
    
    def height(self, root):
        if root is None:
            return 0
        return max(binaryTree.height(root.left), binaryTree.height(root.right))+1

    def numberOfNodes(self, root):
        if root is None:
            return 0
        return binaryTree.numberOfNodes(root.left)+binaryTree.numberOfNodes(root.right)+1

    def numberOfLeafs(self, root):

        if (root.left and root.right) is None:
            return 1
        return binaryTree.numberOfLeafs(root.left)+binaryTree.numberOfLeafs(root.right)
    
    def lastElement(self, root):

        if (root.right and root.left) is None:
            return root
        if root.right is None:
            binaryTree.lastElement(root.left)
        else:
            binaryTree.lastElement(root.right)
    # def findMin(self, root):
    #     if root.left > root.right:


root = Node(5)
root.left = Node(11)
root.left.left = Node(17)
root.right = Node(6)
root.right.left = Node(15)
root.right.right = Node(8)
root.right.right.left = Node(23)
root.right.right.right = Node(45)
binaryTree = binaryTree(root)

#     5
#    /  \
#  11     6
#   /   /  \
# 17   15    8
#           / \
#         23   45

print("preorder traversal before insertion:")
print(binaryTree.preorderTraversal(root))

# # key = 12
# # binaryTree.insert(key)

# # print()
# # print("Inorder traversal after insertion:")
# # binaryTree.inorderTraversal(root)
# print()
# print(binaryTree.height(root))
# print(binaryTree.numberOfLeafs(root))
# # binaryTree.deleteRoot()
# print(binaryTree.preorderTraversal(root))
print(binaryTree.lastElement(root))