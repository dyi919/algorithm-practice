# https://www.acmicpc.net/problem/14891

from sys import stdin

ans = 0
gears = [[0] * 8 for _ in range(4)]
for i in range(4):
    gears[i] = [int(x) for x in stdin.readline().strip()]
K = int(input())
rotates = [[0] * 2 for _ in range(K)]
for i in range(K):
    rotates[i] = [int(x) for x in stdin.readline().split()]

for gear, direction in rotates:
    gear -= 1
    directions = [0] * 4
    directions[gear] = direction
    for i in range(gear, 0, -1):
        if gears[i-1][2] != gears[i][6]:
            directions[i-1] = -directions[i]
    for i in range(gear, 3):
        if gears[i+1][6] != gears[i][2]:
            directions[i+1] = -directions[i]
    for i in range(4):
        if directions[i] == 0:
            continue
        if directions[i] == -1:
            gears[i] = gears[i][1:]+[gears[i][0]]
        if directions[i] == 1:
            gears[i] = [gears[i][-1]]+gears[i][:-1]

for i in range(4):
    ans += gears[i][0] * (2**i)

print(ans)
