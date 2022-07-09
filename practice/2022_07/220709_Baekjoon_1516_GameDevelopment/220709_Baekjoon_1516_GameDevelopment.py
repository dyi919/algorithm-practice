# https://www.acmicpc.net/problem/1516

from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
time = [0] * (N+1)
indegree = [0] * (N+1)
cache = [0] * (N+1)

for i in range(1, N+1):
    line = list(map(int, input().split()))[:-1]
    time[i] = line[0]
    line_length = len(line)
    if line_length > 1:
        indegree[i] += line_length - 1
        for pre in line[1:]:
            tree[pre].append(i)

queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        cache[i] = time[i]
        queue.append(i)

while queue:
    current = queue.popleft()
    for next in tree[current]:
        cache[next] = max(cache[current] + time[next], cache[next])
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, N+1):
    print(cache[i])
