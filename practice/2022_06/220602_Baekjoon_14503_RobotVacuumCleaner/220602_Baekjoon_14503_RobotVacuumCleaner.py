# https://www.acmicpc.net/problem/14503

from sys import stdin

direction_row, direction_col = [-1, 0, 1,
                                0], [0, 1, 0, -1]  # north, east, south, west
N, M = [int(x) for x in stdin.readline().split()]
# direction - 0: north, 1: east, 2: south, 3: west
row, col, direction = [int(x) for x in stdin.readline().split()]
board = [[0] * M for _ in range(N)]
for i in range(N):
    board[i] = [int(x) for x in stdin.readline().split()]
ans = 0

while True:
    if board[row][col] == 0:
        board[row][col] = 2
        ans += 1
    count = 0
    while count < 4:
        if direction == 0:
            direction = 3
        else:
            direction -= 1
        next_row, next_col = row + \
            direction_row[direction], col+direction_col[direction]
        if board[next_row][next_col] == 0:
            break
        count += 1
    if count == 4:
        prev_row, prev_col = row - \
            direction_row[direction], col-direction_col[direction]
        if board[prev_row][prev_col] == 1:
            break
        else:
            row, col = prev_row, prev_col
    else:
        row, col = next_row, next_col

print(ans)
