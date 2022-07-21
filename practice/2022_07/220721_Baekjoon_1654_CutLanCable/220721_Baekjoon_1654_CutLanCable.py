# https://www.acmicpc.net/problem/1654

from sys import stdin
input = stdin.readline

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

lo, hi = 1, max(cables)
mid = 0
count = 0

while lo <= hi:
    mid = (lo + hi) // 2
    count = sum([cable // mid for cable in cables])
    if count < N:
        hi = mid - 1
    else:
        lo = mid + 1

print(hi)