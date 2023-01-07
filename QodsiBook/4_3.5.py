class Node:
    def __init__(self, char):
        self.next = None
        self.updown = None
        self.char = char
        self.rthread = 0
        self.uthread = 0

expression = '((ab)cd)'
def lispList(expression):
    '''convert expression to lisp list'''
    root = Node(expression[0])
    current = root
    for i in range(1,len(expression)-1):
        if expression[i] == '(':
            
            current.updown = Node(expression[i])
            temp = current
            current = current.updown
            current.updown = temp
            current.uthread = 1
            rootOfStage = current
            print(i," ",current.char," ", current.updown," ", current.next)
        elif expression[i] == ')':
            current.next = rootOfStage
            current.rthread = 1
            current = rootOfStage.updown
            
        else:
            current.next = Node(expression[i])
            current = current.next
    return root
root = lispList(expression)
# def printLispList(root):
#     '''print lisp list'''
#     current = root
#     while current:
#         print(current.char, end=" ")
#         if current.rthread == 0:
#             current = current.next
#         if:
#             current = current.updown
#             while current.uthread == 1:
#                 current = current.updown
#             current = current.next
# printLispList(root)