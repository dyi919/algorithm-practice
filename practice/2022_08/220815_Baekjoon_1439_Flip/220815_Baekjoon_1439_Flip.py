# https://www.acmicpc.net/problem/1439

from sys import stdin
input = stdin.readline

S = input().strip()
section = [0, 0]

section[int(S[0])] = 1
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        section[int(S[i])] += 1

print(min(section))