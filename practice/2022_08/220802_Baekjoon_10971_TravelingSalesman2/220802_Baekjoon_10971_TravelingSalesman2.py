# https://www.acmicpc.net/problem/10971

from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit = 10**6

N = int(input())
W = [[0] * N for _ in range(N)]

for i in range(N):
    W[i] = list(map(int, input().split()))

ans = 10**7+1
visited = [False] * N

def dfs(city, cost, visited):
    global ans

    if False not in visited[1:N] and W[city][0] > 0:
        ans = min(ans, cost+W[city][0])

    for i in range(1, N):
        if not visited[i] and W[city][i] > 0 and cost+W[city][i] < ans:
            visited[i] = True
            dfs(i, cost+W[city][i], visited)
            visited[i] = False

for i in range(N):
    if W[0][i] > 0:
        visited[i] = True
        dfs(i, W[0][i], visited)
        visited[i] = False

print(ans)