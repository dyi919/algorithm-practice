# https://www.acmicpc.net/problem/1916

from sys import stdin, maxsize
import heapq

N = int(input())
M = int(input())
edges = [[] for _ in range(N+1)]
dist = [maxsize] * (N+1)
for i in range(M):
    A, B, C = [int(x) for x in stdin.readline().split()]
    edges[A].append((B, C))

start, end = [int(x) for x in stdin.readline().split()]
dist[start] = 0
pq = []

heapq.heappush(pq, (0, start))

while pq:
    cost, node = heapq.heappop(pq)
    if dist[node] < cost:
        continue
    for v, d in edges[node]:
        nextDist = dist[node] + d
        if nextDist < dist[v]:
            dist[v] = nextDist
            heapq.heappush(pq, (nextDist, v))
    
print(dist[end])
