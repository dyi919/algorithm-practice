# https://www.acmicpc.net/problem/1753

import sys, heapq

V, E = map(int, sys.stdin.readline().split())
K = int(input())
edges = [[] for _ in range(V+1)]
dist = [sys.maxsize] * (V+1)
dist[K] = 0

for _ in range(E):
    f, t, c = map(int, sys.stdin.readline().split())
    edges[f].append((t, c))

pq = []
heapq.heappush(pq, (0, K))

while pq:
    cost, node = heapq.heappop(pq)
    if dist[node] < cost:
        continue
    for v, d in edges[node]:
        nextDist = dist[node]+d
        if nextDist < dist[v]:
            dist[v] = nextDist
            heapq.heappush(pq, (nextDist, v))
        
for i in range(1, V+1):
    if dist[i] == sys.maxsize:
        print("INF")
    else:
        print(dist[i])