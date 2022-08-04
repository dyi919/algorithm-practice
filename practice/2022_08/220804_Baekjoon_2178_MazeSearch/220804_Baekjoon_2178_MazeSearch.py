# https://www.acmicpc.net/problem/2178

from sys import stdin
from collections import deque
input = stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N, M = map(int, input().split())
maze = [[] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
for i in range(N):
    maze[i] = list(input().strip())

queue = deque()
queue.append([0, 0, 1])
visited[0][0] = True

while queue:
    x, y, step = queue.popleft()
    if x == N-1 and y == M-1:
        print(step)
        break
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == '1' and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append([nx, ny, step+1])
