# https://www.acmicpc.net/problem/1309

from sys import stdin
input = stdin.readline

MOD = 9901
N = int(input())
cache = [[0] * 2 for _ in range(N+2)]
cache[1] = [1, 1]

for i in range(2, N+2):
    cache[i] = [(cache[i-1][0] + cache[i-1][1]*2) % MOD, (cache[i-1][0] + cache[i-1][1]) % MOD]

print(cache[N+1][0])