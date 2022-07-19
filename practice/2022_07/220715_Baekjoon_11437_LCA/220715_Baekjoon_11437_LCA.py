# https://www.acmicpc.net/problem/11437

from sys import stdin, setrecursionlimit
setrecursionlimit(int(1e5))
input = stdin.readline
HEIGHT = 18

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [[0] * HEIGHT for _ in range(N+1)]
visited = [False] * (N+1)
depth = [0] * (N+1)

for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(x, d):
    visited[x] = True
    depth[x] = d
    for child in graph[x]:
        if not visited[child]:
            parent[child][0] = x
            dfs(child, d+1)

def set_parent():
    dfs(1, 0)
    for i in range(1, HEIGHT):
        for j in range(1, N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]
        
def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(HEIGHT-1, -1, -1):
        if depth[b] - depth[a] >= 2**i:
            b = parent[b][i]
    
    if a == b:
        return a
    
    for i in range(HEIGHT-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a, b = parent[a][i], parent[b][i]

    return parent[a][0]

set_parent()

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
