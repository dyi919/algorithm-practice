# https://www.acmicpc.net/problem/15486

from sys import stdin

N = int(input())
T = []
P = []
for _ in range(N):
    t, p = [int(x) for x in stdin.readline().split()]
    T.append(t)
    P.append(p)

cache = [0] * (N+1)

for i in range(N):
    cache[i] = max(cache[i], cache[i-1])
    if i+T[i] <= N:
        cache[i+T[i]] = max(cache[i+T[i]], cache[i] + P[i])
cache[N] = max(cache[N-1], cache[N])

print(cache[N])

