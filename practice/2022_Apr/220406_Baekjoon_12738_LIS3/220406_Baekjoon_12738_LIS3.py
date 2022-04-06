# https://www.acmicpc.net/problem/12738

from bisect import bisect_left
from sys import stdin

N = int(input())
A = [int(x) for x in stdin.readline().split()]
length = 1
tail = [0] * (N+1)
tail[0] = A[0]

for i in range(1, N):
    if A[i] > tail[length-1]:
        tail[length] = A[i]
        length += 1
    else:
        tail[bisect_left(tail, A[i], 0, length-1)] = A[i]

print(length)