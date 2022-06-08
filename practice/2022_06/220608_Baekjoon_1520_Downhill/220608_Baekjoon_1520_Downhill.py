# https://www.acmicpc.net/problem/1520

from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

M, N = [int(x) for x in stdin.readline().split()]
board = [[0] * N for _ in range(M)]
for i in range(M):
    board[i] = [int(x) for x in stdin.readline().split()]
cache = [[-1] * N for _ in range(M)]

def dfs(r, c):  
    if [r, c] == [M-1, N-1]:
        return 1
    if cache[r][c] != -1:
        return cache[r][c]

    cache[r][c] = 0 
    for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        new_r, new_c = r+i, c+j
        if 0 <= new_r < M and 0 <= new_c < N:
            if board[new_r][new_c] < board[r][c]:
                cache[r][c] += dfs(new_r, new_c)   
    return cache[r][c]

dfs(0, 0)
print(cache[0][0])