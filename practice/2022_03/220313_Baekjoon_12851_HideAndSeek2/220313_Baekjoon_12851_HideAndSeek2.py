# https://www.acmicpc.net/problem/12851

from sys import stdin
import collections

N, K = [int(i) for i in stdin.readline().split()]
if N > K:
    print(N-K)
    print(1)
else: 
    q = collections.deque()
    visited = [[-1, 0] for _ in range(100001)]
    visited[N] = [0, 1]
    q.append(N)

    while q:
        x = q.popleft()
        for nx in (x+1, x-1, x*2):
            if 0 <= nx < 100001:
                if visited[nx][0] == -1:
                    visited[nx][0] = visited[x][0] + 1
                    visited[nx][1] = visited[x][1]
                    q.append(nx)
                elif visited[nx][0] == visited[x][0] + 1:
                    visited[nx][1] += visited[x][1]

    print(visited[K][0])
    print(visited[K][1])