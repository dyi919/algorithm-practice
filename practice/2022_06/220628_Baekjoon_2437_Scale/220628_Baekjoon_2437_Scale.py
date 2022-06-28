# https://www.acmicpc.net/problem/2437

from sys import stdin
input = stdin.readline

N = int(input())
weight = sorted([int(x) for x in input().split()])

ans = 1

for i in range(N):
    if ans < weight[i]:
        break
    ans += weight[i]
    
print(ans)