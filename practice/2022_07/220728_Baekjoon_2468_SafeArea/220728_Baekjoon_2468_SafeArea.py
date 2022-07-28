# https://www.acmicpc.net/problem/2468

from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
safe = []
ans = 1
max_height = max(map(max, area))
min_height = min(map(min, area))

def dfs(x, y, height):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and area[nx][ny] > height:
            visited[nx][ny] = True
            dfs(nx, ny, height)

for current_height in range(min_height, max_height):
    safe = []
    visited = [[False] * N for _ in range(N)]
    num_safe_area = 0

    for i in range(N):
        for j in range(N):
            if area[i][j] > current_height:
                safe.append((i, j))
    
    for x, y in safe:
        if not visited[x][y]:
            visited[x][y] = True
            dfs(x, y, current_height)
            num_safe_area += 1

    ans = max(ans, num_safe_area)

print(ans)