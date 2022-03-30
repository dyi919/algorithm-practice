# https://www.acmicpc.net/problem/7579

from sys import stdin, maxsize

N, M = [int(x) for x in stdin.readline().split()]
m = [int(x) for x in stdin.readline().split()]
c = [int(x) for x in stdin.readline().split()]
total_cost = sum(c)
cache = [-1] * (total_cost+1)
cache[0] = 0

for i in range(N):
    for j in range(total_cost, c[i]-1, -1):
        if cache[j-c[i]] != -1:
            cache[j] = max(cache[j-c[i]] + m[i], cache[j])

for i in range(total_cost+1):
    if cache[i] >= M:
        print(i)
        break
