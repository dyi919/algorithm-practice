# https://www.acmicpc.net/problem/11656

from sys import stdin
input = stdin.readline

S = list(input().strip())
ans = sorted([S[i:] for i in range(len(S))])
for word in ans:
    print(''.join(word))