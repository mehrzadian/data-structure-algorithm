class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFS(self, temp, v, visited):

        visited[v] = True
        temp.append(v)

        for i in self.adj[v]:
            if visited[i] == False:
                temp = self.DFS(temp, i, visited)
        return temp
    # if the graph is connected , it will return true and will go to dfs for printing
    # the spanning tree

    def spanningTree(graph):
        if len(graph.connectedComponents()) > 1:
            print("Graph is not connected")
            return False

        visited = [False] * (graph.V)
        print(graph.adj)
        for ls in graph.adj:
            for i in ls:
                if visited[i] == False:
                    visited[i] = True
                    print(i, end=" ")
        return True

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def getAdjOf(self, v):
        return self.adj[v]

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFS(temp, v, visited))
        return cc

 # make adjacency matrix for each connected component


def adjacencyMatrix(connectedComponents):
    adjacencyMatrix = []
    for i in range(len(connectedComponents)):
        adjacencyMatrix.append([])
        x = len(connectedComponents[i])
        for j in range(x):
            adjacencyMatrix[i].append([0]*x)
    for i in range(len(connectedComponents)):
        for j in range(len(connectedComponents[i])):
            for k in range(len(connectedComponents[i])):
                if connectedComponents[i][j] in g.getAdjOf(connectedComponents[i][k]):
                    adjacencyMatrix[i][j][k] = 1

    return adjacencyMatrix

 # example 1
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(2, 1)
g.addEdge(3, 4)
g.addEdge(0, 2)
g.addEdge(3, 0)
print("spanning Tree")
g.spanningTree()
print()
# example 2  graph is not connected , vertex 5 is not connected to any other vertex
g = Graph(10)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(0, 4)
g.addEdge(6, 7)
g.addEdge(6, 8)
g.addEdge(6, 9)
g.addEdge(7, 8)
g.addEdge(8, 9)
print("spanning Tree")
g.spanningTree()
