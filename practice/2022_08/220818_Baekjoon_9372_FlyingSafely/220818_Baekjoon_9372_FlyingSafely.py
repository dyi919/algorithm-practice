# https://www.acmicpc.net/problem/9372 

from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    for _ in range(m):
        input()
    print(n-1)