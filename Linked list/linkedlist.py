class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def printll(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    def pushAtFirst(self,data):
        node=Node(data)
        node.next = self.head
        self.head =node
    def pushAtPos(self,prevNode,newData):
        if prevNode is None:
            print("previous node doesn't exist!")
        newNode =Node(newData)
        newNode.next=prevNode.next
        prevNode.next=newNode
    def pushAtEnd(self,data):
        node=Node(data)
        temp=self.head
        while temp.next:
            temp = temp.next
        temp.next=node