from sys import stdin
from collections import deque
input = stdin.readline

dx, dy = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]
T = int(input())

for _ in range(T):
    L = int(input())
    fromX, fromY = map(int, input().split())
    toX, toY = map(int, input().split())
    visited = [[False] * L for _ in range(L)]
    queue = deque()
    queue.append((fromX, fromY, 0))
    visited[fromX][fromY] = True
    while queue:
        x, y, moves = queue.popleft()
        if x == toX and y == toY:
            print(moves)
            break
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < L and 0 <= ny < L and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves+1))
