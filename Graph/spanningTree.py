import sys
# I get the graph as incidence matrix
# what is incidence matrix? ---->   https://en.wikipedia.org/wiki/Incidence_matrix
#     v1 v2 v3 v4
#  e1 1  0  0   1
#  e2 1  1  0   0
#  e3 0  0  1   1
#
v, e = map(int,input().split()) #number of vertices and edges
graph = [[0]*v for i in range(e)]
print(graph)
print("In following line give me each vertices that are connected like this format:\\n",
    "1-2 1-3 2-4 2-5\\n ")
edges =input().split()
def checkCorrectness(edges,v,e):
    if len(edges) != e:
        print('you can only have {} edges! Try one more time.'.format(e))
        edges =input().split()

    checkV=list(range(1,v+1)) 
    # check if there is correct number of vertices
    for item in edges:
        x=item.split('-')
        if x[0]==x[1]:
            sys.exit('vertice cant have an edge to themselves! Try again')
            
        if all(1<= int(ele) <= v for ele in x) is False:
            sys.exit('you can only have vertices from 1 to {}! Try again'.format(v))
    
checkCorrectness(edges,v,e)

def matrixIncidence(edges):
    for i,item in enumerate(edges):
        x= item.split('-')
        graph[i][int(x[0])-1]=1
        graph[i][int(x[1])-1]=1
    
matrixIncidence(graph)

# def inorder(self, root):
    #     if root:
    #         self.inorder(root.left)
    #         print(root.val)
    #         self.inorder(root.right)

    # def preorder(self, root):
    #     if root:
    #         print(root.val)
    #         self.preorder(root.left)
    #         self.preorder(root.right)

    # def postorder(self, root, q=[]):
    #     if root:
    #         self.postorder(root.left, q)
    #         self.postorder(root.right, q)

    #         q.append(root)

    #     q = [i for i in q if i.val == None]
    #     return q










    # def smallestChild(self, node):
    #     if node.left == None and node.right == None:
    #         return
    #     return node.left

    # def largestChild(self, node):
    #     if node.left == None and node.right == None:
    #         return
    #     return node.right

    # def displace(self):
    #     x = self.smallestChild(self)
    #     y = self.largestChild(self)
    #     if y.val - x.val == -1:
    #         self.right, self.left = self.left, self.right
    #         return 1
    #     elif y.val - x.val < -1:
    #         return False
    #     elif y.val - x.val > 1:
    #         return False
    #     return True