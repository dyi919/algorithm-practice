# https://www.acmicpc.net/problem/11727

from sys import stdin
input = stdin.readline

MOD = 10007
n = int(input())
cache = [1] * (n+1)
cache[1] = 1

for i in range(2, n+1):
    cache[i] = (cache[i-1] + cache[i-2] * 2) % MOD

print(cache[n])