# Given a singly linked list and a key, count the number of occurrences of the given key in the linked list.
# For example,
# if the given linked list is 1->2->1->2->1->3->1 and the given key is 1, then the output should be 4
from linkedlist import *
linkedlist1=LinkedList()
size = int(input())
data = input()
node = Node(data)
linkedlist1.head=node
for i in range(size-1):
    data = input()
    linkedlist1.pushAtEnd(data)
# linkedlist1.printll()
key = input("what key do you want to count?\n")
def numberOfOccurance(linkedlist1, key):
    count=0
    temp = linkedlist1.head
    while temp:
        if temp.data is key:
            count+=1
        temp = temp.next
    print("{} is repeated {} times".format(key,count))

numberOfOccurance(linkedlist1,key)