# https://www.acmicpc.net/problem/7576

from sys import stdin
from collections import deque
input = stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
M, N = [int(x) for x in input().split()]
box = []
queue = deque()
tomato_left = 0
ans = 1

for i in range(N):
    box.append([int(x) for x in input().split()])
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j])
        elif box[i][j] == 0:
            tomato_left += 1

while queue:
    x, y = queue.popleft()

    for i in range(4):
        new_x, new_y = x+dx[i], y+dy[i]
        if 0 <= new_x < N and 0 <= new_y < M:
            if box[new_x][new_y] == 0:
                ans = max(ans, box[x][y]+1)
                box[new_x][new_y] = box[x][y]+1
                tomato_left -= 1
                queue.append([new_x, new_y])

print(-1 if tomato_left != 0 else ans-1)