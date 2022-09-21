# https://www.acmicpc.net/problem/11404

from sys import stdin
import heapq
input = stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))

for i in range(n+1):
    edges[i].sort()
    edges[i].reverse()
    edges[i] = list(dict(edges[i]).items())

for i in range(1, n+1):
    dist = [INF] * n
    dist[i-1] = 0
    pq = []
    heapq.heappush(pq, [0, i])
    while pq:
        c, v = heapq.heappop(pq)
        for nv, nc in edges[v]:
            nc += c
            if nc < dist[nv-1]:
                dist[nv-1] = nc
                heapq.heappush(pq, [nc, nv])
    for d in dist:
        print(d if d < INF else 0, end=" ")
    print()
