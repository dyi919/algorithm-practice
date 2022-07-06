# https://www.acmicpc.net/problem/1937

from sys import stdin
input = stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0
n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
cache = [[0] * n for _ in range(n)]

def move(x, y):
    if cache[x][y] != 0:
        return cache[x][y]
    cache[x][y] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if forest[x][y] < forest[nx][ny]:
                cache[x][y] = max(cache[x][y], move(nx, ny) + 1)
    return cache[x][y]

for i in range(n):
    for j in range(n):
        ans = max(ans, move(i, j))

print(ans)