# https://www.acmicpc.net/problem/14500

from sys import stdin

ans = 0
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

N, M = [int(x) for x in stdin.readline().split()]
board = [[0] * M for _ in range(N)]

for i in range(N):
    board[i] = [int(x) for x in stdin.readline().split()]


def dfs(start, prev, depth):
    if depth == 4:
        return 0

    max_val = 0

    for i in range(4):
        next = [start[0]+dy[i], start[1]+dx[i]]
        if next[0] < 0 or next[0] >= N or next[1] < 0 or next[1] >= M or next == prev:
            continue
        else:
            max_val = max(max_val, dfs(next, start, depth+1))

    if depth == 1:
        diff = [prev[0] - start[0], prev[1] - start[1]]
        t_values = []
        for i in range(4):
            if diff == [dy[i], dx[i]]:
                continue
            else:
                next = [start[0]+dy[i], start[1]+dx[i]]
                if next[0] < 0 or next[0] >= N or next[1] < 0 or next[1] >= M:
                    continue
                t_values.append(board[next[0]][next[1]])
        if len(t_values) > 1:
            max_t = max(t_values)
            t_values.remove(max_t)
            max_t += max(t_values)
            max_val = max(max_val, max_t)

    return board[start[0]][start[1]] + max_val


for i in range(N):
    for j in range(M):
        depth = 0
        start = [i, j]
        ans = max(ans, dfs(start, start, 0))

print(ans)
