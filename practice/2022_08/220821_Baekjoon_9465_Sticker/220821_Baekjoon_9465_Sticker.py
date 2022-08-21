# https://www.acmicpc.net/problem/9465

from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    cache = [[0] * 3 for _ in range(n+1)]

    for i in range(1, n+1):
        cache[i][0] = max(cache[i-1][1], cache[i-1][2]) + stickers[0][i-1]
        cache[i][1] = max(cache[i-1][0], cache[i-1][2]) + stickers[1][i-1]
        cache[i][2] = max(cache[i-1][0], cache[i-1][1])
    
    print(max(cache[n]))