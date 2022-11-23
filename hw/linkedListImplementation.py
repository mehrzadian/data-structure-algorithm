class Node:

    def __init__(self,value):
        self.value=value
        self.next=None


class linkedList:

    def __init__(self,value=None):
        self.head=Node(value)

    def pushAtFirst(self,value):
        node = Node(value)
        node.next = self.head
        self.head=node

    def push(self,value):
        newNode=Node(value)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
    def print(self):
        temp = self.head
        while temp:
            print(temp.value , end=" ")
            temp = temp.next
        print()
if __name__ == '__main__':
    ll = linkedList()

    ll.print()
    ll.push(10)
    ll.push("amirreza")
    ll.pushAtFirst("hi")
    ll.print()