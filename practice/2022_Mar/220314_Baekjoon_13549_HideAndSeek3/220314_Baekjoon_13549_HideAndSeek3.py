# https://www.acmicpc.net/problem/13549

from sys import stdin
import collections

def bfs():
    visited[N] = 0
    q.append(N)

    while q:
        x = q.popleft()
        if x == K:
            return visited[x]
        if x*2 < 100001:
            if visited[x*2] == -1:
                visited[x*2] = visited[x]
                q.appendleft(x*2)
            else:
                visited[x*2] = min(visited[x*2], visited[x])
        for nx in (x+1, x-1):
            if 0 <= nx < 100001:
                if visited[nx] == -1:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
                else:
                    visited[nx] = min(visited[nx], visited[x] + 1)

N, K = [int(i) for i in stdin.readline().split()]
if N > K:
    print(N-K)
else: 
    q = collections.deque()
    visited = [-1] * 100001
    
    print(bfs())