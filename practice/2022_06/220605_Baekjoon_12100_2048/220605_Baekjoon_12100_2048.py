# https://www.acmicpc.net/problem/12100

from sys import stdin
from collections import deque

def merge(new_board, direction):
    new_board = rotate(new_board, direction)
    for i in range(N):
        j = 1
        merged = [False] * N
        while j < N:
            if new_board[i][j-1] == 0:
                count = 1
                while j-1+count < N and new_board[i][j-1+count] == 0:
                    count += 1
                if j-1+count < N:
                    for k in range(j-1, N-count):
                        new_board[i][k] = new_board[i][k+count]
                    for k in range(N-1, N-count-1, -1):
                        new_board[i][k] = 0
            j += 1
        j = 1
        while j < N:
            if new_board[i][j-1] == new_board[i][j] and not merged[j-1]:
                new_board[i][j-1] *= 2
                for k in range(j+1, N):
                    new_board[i][k-1] = new_board[i][k]
                new_board[i][N-1] = 0
                merged[j-1] = True
            j += 1
    new_board = rotate(new_board, 4-direction)
    return new_board

def rotate(new_board, direction):
    if direction in [0, 4]:
        return new_board
    
    for _ in range(direction):
        new_board = rotated(new_board)

    return new_board

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

N = int(input())
board = [[0] * N for _ in range(N)]

for i in range(N):
    board[i] = [int(x) for x in stdin.readline().split()]

ans = 0
queue = deque()
queue.append([board, 0])

while queue:
    current_board, depth = queue.popleft()
    for i in range(4):
        new_board = merge([x[:] for x in current_board], i)
        ans = max(ans, max([max(x) for x in new_board]))
        if depth < 4:
            queue.append([new_board, depth+1])

print(ans)