# https://www.acmicpc.net/problem/1789

from sys import stdin
input = stdin.readline

S = int(input())
ans = 0
val_sum = 0

for i in range(1, S+1):
    val_sum += i
    if val_sum > S:
        break
    else:
        ans += 1

print(ans)