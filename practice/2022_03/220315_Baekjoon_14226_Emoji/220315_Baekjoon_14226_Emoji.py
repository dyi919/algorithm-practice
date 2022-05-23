# https://www.acmicpc.net/problem/14226

import collections

N = int(input())
visited = [[-1] * (1002) for _ in range(1002)]
visited[1][0] = 0
q = collections.deque([(1, 0)])
while q:
    num, clipboard = q.popleft()
    if num == N:
        print(visited[num][clipboard])
        break
    if num-1 > 1 and visited[num-1][clipboard] == -1:
            visited[num-1][clipboard] = visited[num][clipboard] + 1
            q.append((num-1, clipboard))
    if num+clipboard < 1002 and visited[num+clipboard][clipboard] == -1:
        visited[num+clipboard][clipboard] = visited[num][clipboard] + 1
        q.append((num+clipboard, clipboard))
    if visited[num][num] == -1:
        visited[num][num] = visited[num][clipboard] + 1
        q.append((num, num))
