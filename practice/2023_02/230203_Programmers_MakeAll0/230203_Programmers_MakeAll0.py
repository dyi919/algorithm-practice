# https://school.programmers.co.kr/learn/courses/30/lessons/76503

import sys
sys.setrecursionlimit(300000)

def solution(a, edges):
    if sum(a) != 0: return -1

    N = len(a)
    graph = [[] for _ in range(N)]
    visited = [False] * N
    answer = 0
    
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    def dfs(v):
        nonlocal answer

        visited[v] = True
        
        for n in graph[v]:
            if not visited[n]:
                a[v] += dfs(n)
                
        prev = a[v]
        a[v] = 0
        answer += abs(prev)
        
        return prev
        
    return answer if dfs(0) == 0 else -1