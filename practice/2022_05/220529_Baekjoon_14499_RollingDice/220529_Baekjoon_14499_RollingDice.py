# https://www.acmicpc.net/problem/14499

from sys import stdin

N, M, x, y, K = [int(x) for x in stdin.readline().split()]
board = [[0] * M for _ in range(N)]

for i in range(N):
    board[i] = [int(x) for x in stdin.readline().split()]

moves = [int(x) for x in stdin.readline().split()]

dice = {
    "top": 0,
    "bottom": 0,
    "east": 0,
    "west": 0,
    "south": 0,
    "north": 0
}

for move in moves:
    if move == 1:  # east
        if y == M-1:
            continue
        y += 1
        dice["bottom"], dice["east"], dice["top"], dice["west"] = dice["east"], dice["top"], dice["west"], dice["bottom"]
    elif move == 2:  # west
        if y == 0:
            continue
        y -= 1
        dice["bottom"], dice["east"], dice["top"], dice["west"] = dice["west"], dice["bottom"], dice["east"], dice["top"]
    elif move == 3:  # south
        if x == 0:
            continue
        x -= 1
        dice["bottom"], dice["north"], dice["top"], dice["south"] = dice["south"], dice["bottom"], dice["north"], dice["top"]
    else:  # north
        if x == N-1:
            continue
        x += 1
        dice["bottom"], dice["south"], dice["top"], dice["north"] = dice["north"], dice["bottom"], dice["south"], dice["top"]
    if board[x][y] == 0:
        board[x][y] = dice["bottom"]
    else:
        dice["bottom"] = board[x][y]
        board[x][y] = 0
    print(dice["top"])
