# https://www.acmicpc.net/problem/11057

from sys import stdin
input = stdin.readline

N = int(input())
MOD = 10007
cache = [[0] * 10 for _ in range(N+1)]
cache[1] = [1] * 10

for i in range(2, N+1):
    for j in range(10):
        for k in range(j+1):
            cache[i][j] += cache[i-1][k]
        cache[i][j] %= MOD

print(sum(cache[N]) % MOD)
