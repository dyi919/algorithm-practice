# https://www.acmicpc.net/problem/4963

from sys import stdin
from collections import deque
input = stdin.readline

dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]
w, h = map(int, input().split())
while w != 0 and h != 0:
    land = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and land[i][j] == 1:
                ans += 1
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    x, y = queue.pop()
                    for k in range(8):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and land[nx][ny] == 1:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
        
    print(ans)
    w, h = map(int, input().split())