# https://www.acmicpc.net/problem/2212

from sys import stdin

N = int(input())
K = int(input())
sensors = [int(x) for x in stdin.readline().split()]
sensors.sort()
dist = [0] * (N-1)

for i in range(1, N):
    dist[i-1] = sensors[i]-sensors[i-1]

dist.sort()
print(sum(dist[:N-K]) if K < N else 0)