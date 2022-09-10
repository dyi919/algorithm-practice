# https://www.acmicpc.net/problem/2470

from sys import stdin
input = stdin.readline

N = int(input())
solutes = sorted(list(map(int, input().split())))
l, r = 0, N-1
ans = [10 ** 9, 10 ** 9]

while l < r:
    val = solutes[l] + solutes[r]
    ans = [solutes[l], solutes[r]] if abs(val) < abs(ans[0]+ans[1]) else ans
    if val < 0:
        l += 1
    elif val > 0:
        r -= 1
    else:
        break

print(ans[0], ans[1])