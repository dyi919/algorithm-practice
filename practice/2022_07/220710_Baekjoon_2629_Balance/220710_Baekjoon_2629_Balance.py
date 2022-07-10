# https://www.acmicpc.net/problem/2629

from sys import stdin
input = stdin.readline

num_weights = int(input())
weights = list(map(int, input().split()))

cache = [[False] * 15001  for _ in range(num_weights+1)]

def solve(i, w):
    if i > num_weights: return
    if cache[i][w]: return
    cache[i][w] = True
    solve(i+1, w+weights[i-1])
    solve(i+1, abs(w-weights[i-1]))
    solve(i+1, w)

solve(0, 0)

num_marbles = int(input())
marbles = list(map(int, input().split()))

for marble in marbles:
    if marble > 15000: print('N', end=" ")
    elif cache[num_weights][marble]: print('Y', end=" ")
    else: print('N', end=" ")