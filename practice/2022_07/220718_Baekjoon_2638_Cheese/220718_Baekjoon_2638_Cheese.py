# https://www.acmicpc.net/problem/2638

from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N, M = map(int, input().split())
grid = [[] for _ in range(N)]
cheese_count = 0
ans = 0

for i in range(N):
    grid[i] = list(map(int, input().split()))
    for j in range(M):
        if grid[i][j] == 1:
            cheese_count += 1

def air_dfs(x, y):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == 0 and not air[nx][ny]:
                air[nx][ny] = True
                air_dfs(nx, ny)

while cheese_count > 0:
    air = [[False] * M for _ in range(N)]
    air_dfs(0, 0)
    melt = []
    for x in range(1, N-1):
        for y in range(1, M-1):
            if grid[x][y] == 1:
                air_count = 0
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if air[nx][ny]:
                        air_count += 1
                    if air_count >= 2:
                        break
                if air_count >= 2:
                    grid[x][y] = 0
                    cheese_count -= 1
    ans += 1

print(ans)