class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def pushAtFirst(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    def pushAtEnd(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            node.prev = temp
    def pushAtPosition(self, data, index):
        node = Node(data)
        if index == 0:
            self.pushAtFirst(data)
        elif index >= self.size():
            self.pushAtEnd(data)
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            node.next = temp.next
            temp.next.prev = node
            temp.next = node
            node.prev = temp

    def deleteAtFirst(self):
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
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
        del temp
    
    def deleteAtPosition(self, index):
        if index == 0:
            self.deleteAtFirst()
        elif index >= self.size():
            self.deleteAtEnd()
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            temp.next = temp.next.next
            temp.next.prev = temp

    def deleteAtValue(self, data):
        temp = self.head
        if temp.data == data:
            self.deleteAtFirst()
        else:
            while temp.next:
                if temp.next.data == data:
                    temp.next = temp.next.next
                    temp.next.prev = temp
                    break
                temp = temp.next
                del temp
    
    
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
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    def printReverse(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()
    def isEmpty(self):
        return self.head == None
    def size(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    def clear(self):
        self.head = None
    
    def __str__(self):
        temp = self.head
        string = ''
        while temp:
            string += str(temp.data) + ' '
            temp = temp.next
        return string
    def delete(self):
        del self.head
    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.data
            temp = temp.next
    def __len__(self):
        return self.size()
    def __getitem__(self, index):
        if index >= self.size():
            raise IndexError('index out of range')
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.data
    def __setitem__(self, index, data):
        if index >= self.size():
            raise IndexError('index out of range')
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.data = data
    def __delitem__(self, index):
        if index >= self.size():
            raise IndexError('index out of range')
        if index == 0:
            self.deleteAtFirst()
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            del temp
    def __contains__(self, data):
        return self.search(data)
    def __reversed__(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            yield temp.data
            temp = temp.prev
    def __add__(self, other):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = other.head
        other.head.prev = temp
        return self

    def deleteDoublyLinkedList(self):
        temp = self.head
        while temp:
            next = temp.next
            del temp.data
            temp = next
        self.head = None


doublyLinkedList = DoublyLinkedList()
doublyLinkedList.pushAtFirst("َAmirreza Mehrzadian")
doublyLinkedList.pushAtEnd("Computer Engineering")
doublyLinkedList.pushAtEnd("Amirkabir University of Technology")
doublyLinkedList.pushAtEnd("Tehran")
doublyLinkedList.pushAtEnd(40)
doublyLinkedList.pushAtEnd(15)
import random
while doublyLinkedList.size() <100 :
    doublyLinkedList.pushAtEnd(random.randint(1,100))

print(doublyLinkedList)


def reverse(node):
        if node is None:
            
            return 
        node.next, node.prev  = node.prev, node.next
        return reverse(node.prev)
print()
n = Node(1)
n.next = Node(2)
n.next.next = Node(3)
n.next.next.next = Node(4)

n.next.next.next.prev= n.next.next
n.next.next.prev = n.next
n.next.prev = n
reverse(n)
print(n.prev.data)
print()
