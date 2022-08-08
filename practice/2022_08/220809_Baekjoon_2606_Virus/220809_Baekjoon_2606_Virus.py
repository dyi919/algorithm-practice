# https://www.acmicpc.net/problem/2606

from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ans = 0 

num_inputs = int(input())
for _ in range(num_inputs):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)
visited[1] = True

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            ans += 1
            queue.append(neighbor)
            visited[neighbor] = True

print(ans)