# https://www.acmicpc.net/problem/2193

from sys import stdin
input = stdin.readline

N = int(input())
cache = [[0, 0] for _ in range(N+1)]
cache[1] = [0, 1]

if N > 1:
    for i in range(2, N+1):
        cache[i] = [cache[i-1][0] + cache[i-1][1], cache[i-1][0]]

print(sum(cache[N]))