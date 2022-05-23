# https://www.acmicpc.net/problem/1509

from sys import stdin

s = stdin.readline().strip()
L = len(s)
p = [[True if i == j else False for i in range(L)] for j in range(L)]
cache = [-1] * (L+1)
cache[0] = 0
cache[1] = 1

for i in range(1, L):
    p[i-1][i] = True if s[i-1] == s[i] else False

for l in range(2, L+1):
    for i in range(L-l+1):   
        if s[i] == s[i+l-1] and p[i+1][i+l-2]:
            p[i][i+l-1] = True

for i in range(2, L+1):
    for j in range(1, i+1):
        if p[j-1][i-1]:
            if cache[i] == -1 or cache[i] > cache[j-1]+1:
                cache[i] = cache[j-1]+1

print(cache[L])