# https://www.acmicpc.net/problem/1699

from math import sqrt
from sys import stdin
input = stdin.readline

N = int(input())
cache = [x for x in range(N+1)]

for i in range(1, N+1):
    for j in range(1, int(sqrt(i))+1):
        if cache[i-j*j] < cache[i]-1:
            cache[i] = cache[i-j*j] + 1

print(cache[N])