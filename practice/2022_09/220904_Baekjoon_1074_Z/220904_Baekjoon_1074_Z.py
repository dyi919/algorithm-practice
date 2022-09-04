# https://www.acmicpc.net/problem/1074

from sys import stdin
input = stdin.readline

N, r, c = map(int, input().split())
ans = 0

while N > 0:
    len_side = 2 ** N
    quadrant = 0

    if r >= len_side//2:
        quadrant += 2
        r -= len_side//2
    if c >= len_side//2:
        quadrant += 1
        c -= len_side//2

    ans += len_side**2//4 * quadrant
    N -= 1

print(ans)