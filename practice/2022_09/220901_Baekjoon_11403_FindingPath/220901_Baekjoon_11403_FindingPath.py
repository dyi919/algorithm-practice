# https://www.acmicpc.net/problem/11403

from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
G = [list(input().strip().split()) for _ in range(N)]

for i in range(N):
    visited = [False] * N
    for j in range(N):
        if G[i][j] == '1' and not visited[j]:
            visited[j] = True
            queue = deque([j])
            while queue:
                node = queue.popleft()
                for k in range(N):
                    if G[node][k] == '1' and not visited[k]:
                        G[i][k] = '1'
                        visited[k] = True
                        queue.append(k)

for i in range(N):
    print(' '.join(G[i]))