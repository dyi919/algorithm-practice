# https://www.acmicpc.net/problem/11724

from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ans = 0

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

for i in range(1, N+1):
    if not visited[i]:
        visited[i] = True
        queue = deque()
        queue.append(i)
        ans += 1
        while queue:
            node = queue.popleft()
            for neighbor in edges[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

print(ans)