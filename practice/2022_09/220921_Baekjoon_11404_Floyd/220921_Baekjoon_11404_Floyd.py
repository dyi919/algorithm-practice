# https://www.acmicpc.net/problem/11404

from sys import stdin
input = stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

edges = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a-1][b-1] = min(edges[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        if i == k: continue
        for j in range(n):
            if i == j or j == k: 
                continue
            edges[i][j] = min(edges[i][j], edges[i][k]+edges[k][j])

for i in range(n):
    for j in range(n):
        print(edges[i][j] if edges[i][j] < INF else 0, end=" ")
    print()
