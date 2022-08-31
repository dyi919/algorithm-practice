# https://www.acmicpc.net/problem/11055

from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
cache = A.copy()

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            cache[i] = max(cache[i], cache[j] + A[i])

print(max(cache))