# https://www.acmicpc.net/problem/14501

from sys import stdin

N = int(input())
T, P = [0] * (N+1), [0] * (N+1)
cache = [0] * (N+1)

for i in range(1, N+1):
    T[i], P[i] = [int(x) for x in stdin.readline().split()]
    if i + T[i] <= N+1:
        cache[i] = P[i]

for i in range(2, N+1):
    for j in range(1, i):
        if j + T[j] <= i and i + T[i] <= N+1:
            cache[i] = max(P[i] + cache[j], cache[i])

print(max(cache))
