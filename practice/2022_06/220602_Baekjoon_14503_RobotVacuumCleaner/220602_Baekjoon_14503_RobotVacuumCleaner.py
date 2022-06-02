# https://www.acmicpc.net/problem/14503

from sys import stdin

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
N, M = [int(x) for x in stdin.readline().split()]
r, c, d = [int(x) for x in stdin.readline().split()]
board = [[0] * M for _ in range(N)]
for i in range(N):
    board[i] = [int(x) for x in stdin.readline().split()]
ans = 0

while True:
    if board[r][c] == 0:
        board[r][c] = 2
        ans += 1
    count = 0
    while count < 4:
        if d == 0:
            d = 3
        else:
            d -= 1
        next_r, next_c = r+dr[d], c+dc[d]
        if board[next_r][next_c] == 0:
            break
        count += 1
    if count == 4:
        back_r, back_c = r-dr[d], c-dc[d]
        if board[back_r][back_c] == 1:
            break
        else:
            r, c = back_r, back_c
    else:
        r, c = next_r, next_c

print(ans)
