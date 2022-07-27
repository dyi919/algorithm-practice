# https://www.acmicpc.net/problem/1182

from sys import stdin
input = stdin.readline

N, S = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = 0

def solve(sum, i):
    global ans

    if i >= N:
        return

    sum += nums[i]

    if sum == S:
        ans += 1

    solve(sum - nums[i], i+1)
    solve(sum, i+1)

solve(0, 0)
print(ans)