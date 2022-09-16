# https://www.acmicpc.net/problem/1504

from sys import stdin
import heapq
input = stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
edges = [[] for _ in range(N+1)]
dist = [[INF] * (N+1) for _ in range(3)]

for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))
v_list = list(map(int, input().split()))
start = [1] + v_list

for i in range(3):
    pq = []
    dist[i][start[i]] = 0
    heapq.heappush(pq, [0, start[i]])

    while pq:
        c, v = heapq.heappop(pq)
        for nv, nc in edges[v]:
            nc += c
            if nc < dist[i][nv]:
                dist[i][nv] = nc
                heapq.heappush(pq, [nc, nv])

v1_first_dist = dist[0][v_list[0]] + dist[1][v_list[1]] + dist[2][N]
v2_first_dist = dist[0][v_list[1]] + dist[2][v_list[0]] + dist[1][N]
ans = min(v1_first_dist, v2_first_dist)

print(ans if ans < INF else -1)