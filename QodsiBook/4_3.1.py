class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

a0='+1097'
a1='+209'
def linkedlist(a='+2001'):
    if a[0] =='+' or '-':
        head = Node(a[0])
    else:
        head = Node('+')
    nodeList=[]
    for i in range(1,len(a)):
        node = Node(int(a[i]))
        nodeList.append(node)
    head.next = nodeList[len(nodeList)-1]
    nodeList.reverse()
    for i in range(len(nodeList)-1):
        nodeList[i].next = nodeList[i+1]
    return head


def printll(head):
    len = -1
    while head:
        print(head.data)
        head = head.next
        len+=1
    return len


head_a0=linkedlist(a0)
head_a1=linkedlist(a1)
print("len: ",printll(head_a1))

def llsum(head_a0,head_a1):
    
    if printll(head_a1)> printll(head_a0):
        head_a0,head_a1 = head_a1, head_a0
    if head_a0.data == '+':
        nodeh = Node('+')
    else:
        nodeh = Node('-')
    carry = 0
    while head_a1 and head_a0:
        x0 = head_a0.next.data
        x1 = head_a1.next.data
        x2 = (x0+x1)%10 + carry
        carry = (x0+x1)//10
        node =Node(x2)
        temp = nodeh
        while temp:
            temp = temp.next
        temp.next = node
        
        head_a1 = head_a1.next
        head_a0 = head_a0.next
    node =Node(carry)
    temp = nodeh
    while temp:
        temp = temp.next
    temp.next = node
    return printll(nodeh)
print(llsum(a0,a1))








