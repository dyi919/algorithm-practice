# https://www.acmicpc.net/problem/10282

from sys import stdin
import heapq
input = stdin.readline
INF = int(1e9)

T = int(input())

for _ in range(T):
    N, D, C = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    time = [INF] * (N+1)
    
    for _ in range(D):
        a, b, s = map(int, input().split())
        edges[b].append([a, s])
    
    pq = []
    time[C] = 0
    infected = 1
    heapq.heappush(pq, [0, C])

    while pq:
        t, v = heapq.heappop(pq)
        for nv, nt in edges[v]:
            nt += t
            if nt < time[nv]:
                if time[nv] == INF:
                    infected += 1
                time[nv] = nt
                heapq.heappush(pq, [nt, nv])

    print(infected, max([x for x in time if x < INF]))