# https://www.acmicpc.net/problem/1967

from sys import stdin
from collections import deque

input = stdin.readline

ans = 0
n = int(input())
edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e, d = map(int, input().split())
    edges[s].append([e, d])
    edges[e].append([s, d])

def dfs(start):
    stack = deque()
    visited = [False] * (n+1)
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