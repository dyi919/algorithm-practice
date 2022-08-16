# https://www.acmicpc.net/problem/11052

from sys import stdin
input = stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
cache = [0] * (N+1)

for i in range(1, N+1):
    cache[i] = P[i]
    for j in range(i//2+1):
        cache[i] = max(cache[i], cache[i-j]+P[j])

print(cache[N])