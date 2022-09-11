# https://www.acmicpc.net/problem/17070

from sys import stdin
input = stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
cache = [[[0] * 3 for _ in range(N)] for _ in range(N)]
cache[0][1][0] = 1

for i in range(N):
    for j in range(1, N):
        if j+1 < N and house[i][j+1] == 0:
            cache[i][j+1][0] += cache[i][j][0]
            cache[i][j+1][0] += cache[i][j][1]
        if i+1 < N and house[i+1][j] == 0:
            cache[i+1][j][2] += cache[i][j][1]
            cache[i+1][j][2] += cache[i][j][2]
        if j+1 < N and i+1 < N and house[i][j+1] == 0 and house[i+1][j] == 0 and house[i+1][j+1] == 0:
            cache[i+1][j+1][1] += cache[i][j][0]
            cache[i+1][j+1][1] += cache[i][j][1]
            cache[i+1][j+1][1] += cache[i][j][2]

print(sum(cache[N-1][N-1]))
