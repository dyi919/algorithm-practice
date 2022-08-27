from sys import stdin
from collections import deque
input = stdin.readline

N, K = map(int, input().split())

if K <= N:
    print(N-K)
else:
    visited = [-1] * 200001
    visited[N] = 0
    queue = deque([N])

    while queue:
        pos = queue.popleft()

        for next in [pos-1, pos+1, pos*2]:
            if next == K:
                print(visited[pos] + 1)
                break
            if next < 0 or (pos > K and next > pos):
                continue
            if visited[next] < 0:
                visited[next] = visited[pos] + 1
                queue.append(next)
        else:
            continue
        break