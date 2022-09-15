# https://www.acmicpc.net/problem/2665

from sys import stdin
import heapq
input = stdin.readline
INF = int(1e9)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n = int(input())
room = [list(map(lambda x: 1 if x == 0 else 0, list(map(int, list(input().rstrip()))))) for _ in range(n)]
dist = [[INF] * n for _ in range(n)]
dist[0][0] = 0
pq = []

heapq.heappush(pq, [0, 0, 0])
while pq:
    c, x, y = heapq.heappop(pq)
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            nc = c+room[nx][ny]
            if nc < dist[nx][ny]:
                dist[nx][ny] = nc
                heapq.heappush(pq, [nc, nx, ny])

print(dist[n-1][n-1])