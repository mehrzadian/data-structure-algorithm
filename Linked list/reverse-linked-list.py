from linkedlist import *

ll=LinkedList()
size = int(input())
ll.head=Node(input())

for i in range(size-1):
    ll.pushAtEnd(input())




def reverseLinkedList(ll=LinkedList()):
    reversedll = LinkedList()
    temp = ll.printNthFromLast()