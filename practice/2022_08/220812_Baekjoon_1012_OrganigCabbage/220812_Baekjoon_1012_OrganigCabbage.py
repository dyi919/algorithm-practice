# https://www.acmicpc.net/problem/1012

from sys import stdin
from collections import deque
input = stdin.readline

T = int(input())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    visited = [[False] * M for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and field[i][j] == 1:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                ans += 1

                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and field[nx][ny] == 1:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
    
    print(ans)