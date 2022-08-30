# https://www.acmicpc.net/problem/1744

from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

N = int(input())
numbers = sorted([int(input()) for _ in range(N)])
ans = 0
has_zero = True if 0 in numbers else False
has_one = True if 1 in numbers else False
first_zero = bisect_left(numbers, 0)
first_one = bisect_left(numbers, 1)
last_one = bisect_right(numbers, 1)
num_ones = last_one - first_one

if first_zero > 0:
    if first_zero % 2 == 1:
        first_zero -= 1
        if not has_zero:
            ans += numbers[first_zero]
    for i in range(1, first_zero, 2):
        ans += numbers[i-1] * numbers[i]
    
if has_one:
    ans += num_ones

if last_one < N:
    if (N - last_one) % 2 == 1:
        ans += numbers[last_one]
        last_one += 1
    for i in range(last_one, N-1, 2):
        ans += numbers[i] * numbers[i+1]

print(ans)
