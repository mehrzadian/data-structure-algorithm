class Node:
    def __init__(self, data):
        '''In threaded tree, nodes need two more fields which can be 0 or 1 '''
        self.data = data
        self.left = None
        self.right = None
        self.lthread = 0
        self.rthread = 0
