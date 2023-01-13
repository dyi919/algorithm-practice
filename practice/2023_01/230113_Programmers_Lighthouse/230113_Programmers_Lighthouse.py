# https://school.programmers.co.kr/learn/courses/30/lessons/133500

import sys
sys.setrecursionlimit(10 ** 6)

def solution(N, lighthouse):
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node):
        visited[node] = True
        neighbors = [n for n in graph[node] if not visited[n]]
        on, off = 1, 0
    
        for n in neighbors:
            n_on, n_off = dfs(n)
            on += min(n_on, n_off)
            off += n_on
            
        return on, off
        
    return min(dfs(1))