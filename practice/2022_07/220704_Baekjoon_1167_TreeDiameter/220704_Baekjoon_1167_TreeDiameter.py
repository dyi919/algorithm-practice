# https://www.acmicpc.net/problem/1967

from sys import stdin
from collections import deque

input = stdin.readline

ans = 0
V = int(input())
edges = [[] for _ in range(V+1)]

for _ in range(V):
    line = list(map(int, input().split()))
    s = line[0]
    i = 1
    while line[i] != -1:
        edges[s].append([line[i], line[i+1]])
        edges[line[i]].append([s, line[i+1]])
        i += 2

def dfs(start):
    stack = deque()
    visited = [False] * (V+1)
    max_dist = 0
    furthest = 0
    stack.append((start, 0))
    visited[start] = True
    while stack:
        node, val = stack.pop()
        for next_node, dist in edges[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node, val+dist))
        if max_dist < val:
            furthest = node
            max_dist = val
    return (furthest, max_dist)

furthest, _ = dfs(1)
_, ans = dfs(furthest)

print(ans)