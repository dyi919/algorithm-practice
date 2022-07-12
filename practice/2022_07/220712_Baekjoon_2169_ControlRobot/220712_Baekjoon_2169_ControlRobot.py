# https://www.acmicpc.net/problem/2169

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
input = stdin.readline

def solve(x, y, prev_direction):
    if x == N - 1 and y == M - 1:
        return area[x][y]
    
    if cache[x][y][prev_direction] != -1:
        return cache[x][y][prev_direction]
    
    cache[x][y][prev_direction] = -10**9
    for i in range(3):
        if prev_direction + i == 1:
            continue
        new_x, new_y = x+dx[i], y+dy[i]
        if 0 <= new_x < N and 0 <= new_y < M:
            cache[x][y][prev_direction] = max(cache[x][y][prev_direction], solve(new_x, new_y, i) + area[x][y])
    return cache[x][y][prev_direction]

dx, dy = [0, 0, 1], [-1, 1, 0]
N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
cache = [[[-1] * 3 for _ in range(M)] for _ in range(N)]

print(solve(0, 0, 2))
