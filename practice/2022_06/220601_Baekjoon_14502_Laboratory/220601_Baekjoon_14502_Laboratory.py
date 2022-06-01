# https://www.acmicpc.net/problem/14502

from sys import stdin
from collections import deque

N, M = [int(x) for x in stdin.readline().split()]
board, new_board = [[0] * M for _ in range(N)], [[0] * M for _ in range(N)]
viruses = []
walls = []
empty = []
new_walls = [[0, 0], [0, 0], [0, 0]]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]


def bfs():
    safe = len(empty) - 3
    queue = deque()
    for virus in viruses:
        queue.append(virus)

    while queue:
        current_virus = queue.popleft()
        for i in range(4):
            next_virus = [current_virus[0] + dy[i], current_virus[1] + dx[i]]
            if 0 <= next_virus[0] < N and 0 <= next_virus[1] < M and new_board[next_virus[0]][next_virus[1]] == 0:
                new_board[next_virus[0]][next_virus[1]] = 2
                queue.append(next_virus)
                safe -= 1
                if safe < ans:
                    return ans
    return safe


for i in range(N):
    board[i] = [int(x) for x in stdin.readline().split()]
    for j in range(M):
        if board[i][j] == 0:
            empty.append([i, j])
        elif board[i][j] == 1:
            walls.append([i, j])
        else:
            viruses.append([i, j])

ans = 0

for i in range(N*M-2):
    n0, m0 = i // M, i % M
    if [n0, m0] not in empty:
        continue
    new_walls[0] = [n0, m0]
    for j in range(i+1, N*M-1):
        n1, m1 = j // M, j % M
        if [n1, m1] not in empty:
            continue
        new_walls[1] = [n1, m1]
        for k in range(j+1, N*M):
            n2, m2 = k // M, k % M
            if [n2, m2] not in empty:
                continue
            new_walls[2] = [n2, m2]

            new_board = [x[:] for x in board]
            for wall in new_walls:
                new_board[wall[0]][wall[1]] = 1
            ans = max(ans, bfs())

print(ans)
