# https://www.acmicpc.net/problem/5014

from sys import stdin
from collections import deque
input = stdin.readline

f, s, g, u, d = [int(x) for x in input().split()]
visited = [False] * (f+1)
visited[s] = True
queue = deque()
queue.append((s, 0))

while queue:
    current_floor, count = queue.popleft()
    if current_floor == g:
        print(count)
        break
    up = current_floor + u
    down = current_floor - d
    if up <= f:
        if not visited[up]:
            visited[up] = True
            queue.append((up, count + 1))
    if down > 0:
        if not visited[down]:
            visited[down] = True
            queue.append((down, count + 1))
else:
    print("use the stairs")