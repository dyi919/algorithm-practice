# https://www.acmicpc.net/problem/1068

from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)

N = int(input())
parents = list(map(int, input().split()))
delete_node = int(input())

def dfs(num):
    parents[num] = -2
    for i in range(N):
        if num == parents[i]:
            dfs(i)

dfs(delete_node)

count = 0
for i in range(N):
    if parents[i] != -2 and i not in parents:
        count += 1

print(count)