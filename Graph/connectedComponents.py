
class Graph:
    def __init__(self, no):
        self.no = no  # no of nodes
        self.adjlist = [[] for i in range(no)]

    def addEdge(self, f, t):
        self.adjlist[f].append(t)
        self.adjlist[t].append(f)

    def BFS(self, s):
        visited = [0]*self.no
        comp = []
        q = []
        q.append(s)
        visited[s] = 1
        while q:
            s = q.pop()
            comp.append(s)
            for i in self.adjlist[s]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
        return visited, comp

    def allcomponents(self, s, count=0, components=[]):

        v, c = self.BFS(s)
        components.append(c)
        count += 1

        try:
            s = v.index(0)
            return self.allcomponents(s, count, components)
        except ValueError:
            return count, components


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(3, 4)
g.addEdge(2, 1)
print(g.adjlist)
g.BFS(0)
print(g.allcomponents(0))
