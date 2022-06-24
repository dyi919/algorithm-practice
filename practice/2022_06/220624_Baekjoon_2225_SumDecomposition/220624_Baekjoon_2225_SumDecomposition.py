# https://www.acmicpc.net/problem/2225

from sys import stdin

MOD = 10 ** 9
N, K = [int(x) for x in stdin.readline().split()]
cache = [[0] * (N+1) for _ in range(K+1)]
cache[1] = [1] * (N+1)

for i in range(2, K+1):
    for j in range(N+1):
        for k in range(j+1):
            cache[i][j] += cache[i-1][k]
            cache[i][j] %= MOD

print(cache[K][N])
