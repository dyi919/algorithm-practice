# https://www.acmicpc.net/problem/1005

from sys import stdin
from collections import deque
input = stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    tree = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    cache = [0] * (N+1)

    for _ in range(K):
        a, b = map(int, input().split())
        tree[a].append(b)
        indegree[b] += 1
    
    queue = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            cache[i] = D[i]

    while queue:
        current = queue.popleft()
        for i in tree[current]:
            indegree[i] -= 1
            cache[i] = max(cache[current]+D[i], cache[i])
            if indegree[i] == 0:
                queue.append(i)

    win = int(input())
    print(cache[win])