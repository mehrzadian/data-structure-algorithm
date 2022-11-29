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

    def len(self):
        l = 0
        temp = self.head
        while temp:
            l += 1
            temp = temp.next
        return l

    def lenRecursivly(self, head, l=0):
        if not head:
            return l
        l += 1
        return self.lenRecursivly(head.next, l)

    def getLast(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        return temp.data

    def getNth(self, index):
        temp = self.head
        pos = 0
        while pos < index:
            if temp is None:
                print('not found')
                return
            temp = temp.next
            pos += 1
        return temp.data

    def getNthRecussively(self, current, index):
        if index == 0:
            return current.data

        return self.getNthRecussively(current.next, index - 1)

    def printNthFromLast(self, main, ref, n):
        self.getNthRecussively(ref, n)
        while not ref:
            ref = ref.next
            main = main.next
        return main.data

    def numberOfOccurance(self, key):
        count = 0
        temp = self.head
        while temp:
            if temp.data is key:
                count += 1
            temp = temp.next
        print("{} is repeated {} times".format(key, count))

    def __reversed__(self):

        ls = []
        temp = self.head

        while temp:
            ls.append(temp.data)
            temp = temp.next
        ls = ls[::-1]

        reversedLinkedList = LinkedList()
        reversedLinkedList.head = Node(ls[0])
        for i in range(1, len(ls)):
            reversedLinkedList.pushAtEnd(ls[i])
        return reversedLinkedList


if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()
    llist2 = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second  # Link first node with second
    # n=Node(input())
    # llist.head.next=llist.head
    # llist.head.data=n
    second.next = third
    llist.printll()
    llist.pushAtEnd(6)
    llist.pushAtFirst(45)
    # llist.printll()
    # print(llist.getLast())
    # print(llist.searchRecursively(llist.head, 6))
    # print(llist.lenRecursivly(llist.head, 0))
    # print(llist.getNthRecussively(llist.head, 2))
    # print(llist.printNthFromLast(llist.head, llist.head, 3))
    print(reversed(llist))
    llist.printll()
    # print(llist.getLast())
    # llist.deleteAtEnd()
    # print(llist.getLast())
    #
    # llist.deleteAtEnd()
    # print(llist.getLast())
    #
    # llist.deleteAtEnd()
    # print(llist.getLast())
    #
    # llist.deleteAtEnd()
    # print(llist.getLast())
