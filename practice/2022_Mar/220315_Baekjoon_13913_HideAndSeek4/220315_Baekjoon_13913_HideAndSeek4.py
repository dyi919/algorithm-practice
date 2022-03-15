# https://www.acmicpc.net/problem/13913

from sys import stdin
import collections

def bfs():
    while q:
        x = q.popleft()
        if x == K:
            return visited[x]
        for nx in (x+1, x-1, x*2):
            if 0 <= nx < 100001:
                if visited[nx][0] == -1:
                    visited[nx][0] = visited[x][0] + 1
                    visited[nx][1] = x
                    q.append(nx)

N, K = [int(i) for i in stdin.readline().split()]
if N > K:
    print(N-K)
    for i in range(N, K-1, -1):
        print(i, end=" ")
else: 
    q = collections.deque()
    visited = [[-1, -1] for _ in range(100001)]
    visited[N] = [0, -100]
    q.append(N)

    bfs()

    print(visited[K][0])
    path = [K]
    x = K
    while visited[x][1] != -100:
        path.append(visited[x][1])
        x = visited[x][1]
    path.reverse()
    for p in path:
        print(p, end=" ")