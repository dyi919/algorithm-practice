# https://www.acmicpc.net/problem/2583

from sys import stdin
from collections import deque
input = stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
M, N, K = map(int, input().split())
area = [[True] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
ans = []

for _ in range(K):
    bl_x, bl_y, tr_x, tr_y = map(int, input().split())
    for i in range(bl_y, tr_y):
        for j in range(bl_x, tr_x):
            area[i][j] = False

for i in range(M):
    for j in range(N):
        if not visited[i][j] and area[i][j]:
            count = 1
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and area[nx][ny]:
                        visited[nx][ny] = True
                        count += 1
                        queue.append((nx, ny))
            ans.append(count)

print(len(ans))
print(*sorted(ans))