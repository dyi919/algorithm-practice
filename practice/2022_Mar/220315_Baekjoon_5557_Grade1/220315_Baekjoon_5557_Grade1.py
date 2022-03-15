# https://www.acmicpc.net/problem/5557

from sys import stdin

N = int(input())
ls = [int(x) for x in stdin.readline().split()]

cache = [[0] * 21 for _ in range(N)]
cache[0][ls[0]] = 1
for i in range(N-1):
    for j in range(21):
        if cache[i][j] != 0:
            if j+ls[i+1] <= 20:
                cache[i+1][j+ls[i+1]] += cache[i][j]
            if j-ls[i+1] >= 0:
                cache[i+1][j-ls[i+1]] += cache[i][j]
                
print(cache[N-2][ls[-1]])