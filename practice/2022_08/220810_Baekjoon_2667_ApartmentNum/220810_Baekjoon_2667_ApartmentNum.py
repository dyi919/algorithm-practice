# https://www.acmicpc.net/problem/2667

from sys import stdin
from collections import deque
input = stdin.readline

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
N = int(input())
apartment = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
queue = deque()
num_complex = 0
ans_list = []

for i in range(N):
    for j in range(N):
        if apartment[i][j] == '0' or visited[i][j]:
            continue
        num_complex += 1
        queue.append((i, j))
        num_house = 1
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and apartment[nx][ny] == '1':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    num_house += 1
        ans_list.append(num_house)

ans_list.sort()
print(num_complex)
for ans in ans_list:
    print(ans)