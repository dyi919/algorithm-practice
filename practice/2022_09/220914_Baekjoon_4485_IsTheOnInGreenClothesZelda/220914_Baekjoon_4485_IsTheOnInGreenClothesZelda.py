# https://www.acmicpc.net/problem/4485

from sys import stdin
import heapq
input = stdin.readline

INF = int(1e9)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N = int(input())
num_problem = 1

while N != 0 :
    cave = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = cave[0][0]
    ans = 0
    pq = []

    heapq.heappush(pq, [dist[0][0], 0, 0])
    while pq:
        cost, x, y = heapq.heappop(pq)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                nc = cost + cave[nx][ny]
                if nc < dist[nx][ny]:
                    dist[nx][ny] = nc
                    heapq.heappush(pq, [nc, nx, ny])

    print("Problem %d: %d" % (num_problem, dist[N-1][N-1]))
    num_problem += 1
    N = int(input())