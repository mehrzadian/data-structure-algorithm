class Node:
    def __init__(self,data):
        '''In threaded tree, nodes need two more fields which can be 0 or 1 '''
        self.data = data
        self.left = None
        self.right = None
        self.lthread=None
        self.rthread=None
def makeBinTree(preorderTree = 'ABCDEFGHI', inorderTree ='BCAEDGHFI'):
    '''as expalined in page 74 of unit 5 slides,
    find tree and make it from pre-in oreder of it'''
    root = Node(preorderTree[0])
    rootIndex = inorderTree.find(preorderTree[0])
    
    if (len(inorderTree[0:rootIndex]) and len(inorderTree[rootIndex+1:]))==0:
        return root
    
    root.left = makeBinTree(preorderTree[1:1+rootIndex], inorderTree[0:rootIndex])
    root.right = makeBinTree(preorderTree[1+rootIndex:], inorderTree[rootIndex+1:])
    return root

def preorderTraversal(root):
    if root:
        print( root.data, end=" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)

root = makeBinTree()
preorderTraversal(root)


