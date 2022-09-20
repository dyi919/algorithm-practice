from sys import stdin
import heapq
input = stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
edges = [[] for _ in range(n+1)]
total_items = [0] * (n+1)

for _ in range(r):
    a, b, l = map(int, input().split())
    edges[a].append((b, l))
    edges[b].append((a, l))

for i in range(1, n+1):
    dist = [INF] * (n+1)
    pq = []
    dist[i] = 0
    heapq.heappush(pq, [0, i])

    while pq:
        c, v = heapq.heappop(pq)
        for nv, nc in edges[v]:
            nc += c
            if nc < dist[nv] and nc <= m:
                dist[nv] = nc
                heapq.heappush(pq, [nc, nv])
    
    for j in range(1, n+1):
        if dist[j] <= m:
            total_items[i] += items[j]

print(max(total_items))