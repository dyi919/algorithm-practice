# https://www.acmicpc.net/problem/18352

from sys import stdin
from collections import deque
input = stdin.readline
INF = int(1e9)

N, M, K, X = map(int, input().split())
edges = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ans = []

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)

queue = deque()
visited[X] = True
queue.append((X, 0))

while queue:
    v, c = queue.popleft()

    if c == K:
        ans.append(v)
        continue

    for nv in edges[v]:
        if not visited[nv]:
            visited[nv] = True
            queue.append((nv, c+1))

ans.sort()

if len(ans) == 0:
    print(-1)
else:
    for a in ans:
        print(a)