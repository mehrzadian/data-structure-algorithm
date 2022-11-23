class Node:

    def __init__(self,value):
        self.value=value
        self.next=None

class linkedList:

    def __init__(self):
        self.head=None

    def pushAtFirst(self,value):
        node = Node(value)
        node.next = self.head
        self.head=node
