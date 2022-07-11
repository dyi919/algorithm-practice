# https://www.acmicpc.net/problem/1256

from sys import stdin
input = stdin.readline

N, M, K = map(int, input().split())
cache = [[1] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        cache[i][j] = cache[i-1][j] + cache[i][j-1]

if cache[N][M] < K:
    print(-1)
else:
    ans = ""
    while True:
        if N == 0 or M == 0:
            ans += "a" * N
            ans += "z" * M
            break
        flag = cache[N-1][M]
        if K <= flag:
            ans += "a"
            N -= 1
        else:
            ans += "z"
            K -= flag
            M -= 1
    print(ans)
