# https://www.acmicpc.net/problem/2748

from sys import stdin
input = stdin.readline

n = int(input())
cache = [0] * (n+1)
cache[1] = 1

for i in range(2, n+1):
    cache[i] = cache[i-1] + cache[i-2]

print(cache[n])