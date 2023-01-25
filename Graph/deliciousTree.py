t = int(input())
ls = []
for i in range(t):
    m= int(input())
    line = input().split()
    ls.append(line)
print(ls)

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
    def displace(self):
        self.right, self.left = self.left, self.right
        
class Tree:
    def __init__(self,line):
        