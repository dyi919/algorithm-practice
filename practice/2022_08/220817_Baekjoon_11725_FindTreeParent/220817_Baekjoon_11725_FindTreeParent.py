# https://www.acmicpc.net/problem/11725

from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parents = [0] * (N+1)
queue = deque()

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

queue.append(1)
visited[1] = True

while queue:
    node = queue.popleft()
    for child in tree[node]:
        if not visited[child]:
            parents[child] = node
            visited[child] = True
            queue.append(child)

for parent in parents[2:]:
    print(parent)