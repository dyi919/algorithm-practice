from sys import stdin
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def sortEdge(self):
        for v in self.graph:
            self.graph[v].sort()

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

    def BFS(self, v):
        visited = [False] * (max(self.graph) + 1)

        queue = []

        queue.append(v)
        visited[v] = True

        while queue:
            v = queue.pop(0)
            print(v, end=" ")

            for i in self.graph[v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


_, m, v = [int(i) for i in stdin.readline().split()]

g = Graph()
for i in range(m):
    s, e = [int(i) for i in stdin.readline().split()]
    g.addEdge(s, e)
    g.addEdge(e, s)

g.sortEdge()
g.DFS(v)
print()
g.BFS(v)
