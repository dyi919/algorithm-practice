# https://www.acmicpc.net/problem/1449

from sys import stdin
input = stdin.readline

N, L = map(int, input().split())
leak = sorted(list(map(int, input().split())))

if L == 1:
    print(N)
else:
    count = 1
    pos = leak[0]
    for i in range(1, N):
        if leak[i] - pos < L:
            continue
        else:
            count += 1
            pos = leak[i]
    print(count)