class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def pushAtFirst(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pushAtPos(self, prevNode, newData):
        if prevNode is None:
            print("previous node doesn't exist!")
        newNode = Node(newData)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def pushAtEnd(self, data):
        node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def deleteAtFirst(self):
        temp = self.head
        self.head = self.head.next
        del temp

    def deleteAtEnd(self):
        temp = self.head
        prev = None
        if temp == None:
            print('empty')
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None

    def search(self, data):

        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def searchRecursively(self, head, data):
        if not head:
            return False
        if head.data == data:
            return True
        return self.searchRecursively(head.next, data)

    def pushAtEndCircular(self, data):
        node = Node(data)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = node
        node.next = self.head

    def pushAtFirstCircular(self, data):
        node = Node(data)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = node
        node.next = self.head
        self.head = node

    def deleteAtFirstCircular(self):
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

    def deleteAtEndCircular(self):
        temp = self.head
        prev = None
        while temp.next != self.head:
            prev = temp
            temp = temp.next
            prev.next = self.head
    
    def countNodes(self):
        temp = self.head
        count = 0
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count
    
    def findMin(self):
        temp = self.head
        min = temp.data
        while temp.next != self.head:
            if temp.data < min:
                min = temp.data
            temp = temp.next
        return [min,temp]
    
    def findMax(self):
        temp = self.head
        max = temp.data
        while temp.next != self.head:
            if temp.data > max:
                max = temp.data
            temp = temp.next
        return [max,temp]

    
circularLinkedList = circularLinkedList()
circularLinkedList.head = Node(100)
second = Node(2)
third = Node(3)
fourth = Node(66)
fifth = Node(5)
sixth = Node(6)
seventh = Node(7)
eighth = Node(8)
ninth = Node(9)
tenth = Node(10)
circularLinkedList.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = seventh
seventh.next = eighth
eighth.next = ninth
ninth.next = tenth
tenth.next = circularLinkedList.head
print(circularLinkedList.findMin())
