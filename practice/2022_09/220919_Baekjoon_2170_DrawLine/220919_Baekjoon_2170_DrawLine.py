# https://www.acmicpc.net/problem/2170

from sys import stdin
input = stdin.readline

N = int(input())
lines = []

for _ in range(N):
    lines.append(list(map(int, input().split())))

lines.sort()
ans = 0
l, r = -1000000000, -1000000000

for line in lines:
    if r <= line[0]:
        ans += r-l
        l, r = line
    else:
        r = max(r, line[1])
ans += r-l
print(ans)