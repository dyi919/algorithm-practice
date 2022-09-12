# https://www.acmicpc.net/problem/1261

from sys import stdin
import heapq
input = stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
INF = int(1e9)

M, N = map(int, input().split())
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]
dist = [[INF] * M for _ in range(N)]

dist[0][0] = 0
pq = []
heapq.heappush(pq, [0, 0, 0])
while pq:
    c, x, y = heapq.heappop(pq)
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if c+maze[nx][ny] < dist[nx][ny]:
                dist[nx][ny] = c+maze[nx][ny]
                heapq.heappush(pq, [dist[nx][ny], nx, ny])

print(dist[N-1][M-1])
    