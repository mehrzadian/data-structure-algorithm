#given a linkedlist check if it's circular or not
# A linked list is circular if it ends in a node that points to an earlier node in the list.
import linkedlist

def checkIfcircular(linkedlist):
    temp = linkedlist.head
    while temp:
        if temp.next == linkedlist.head:
            return True
        temp = temp.next
