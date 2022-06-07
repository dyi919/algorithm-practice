# https://www.acmicpc.net/problem/2293

from sys import stdin

n, k = [int(x) for x in stdin.readline().split()]
coins = [0] * n
cache = [0] * (k+1)
cache[0] = 1

for i in range(n):
    coins[i] = int(input())

for i in coins:
    for j in range(i, k+1):
        if j-i >= 0:
            cache[j] += cache[j-i]

print(cache[k])