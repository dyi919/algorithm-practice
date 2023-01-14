# https://school.programmers.co.kr/learn/courses/30/lessons/132266

from collections import deque

def solution(N, roads, sources, destination):
    INF = 10 ** 9
    answer = []
    graph = [[] for _ in range(N + 1)]
    distance_from_source = [-1] * (N + 1)
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [False] * (N + 1)
    visited[destination] = True
    distance_from_source[destination] = 0
    queue = deque([(destination, 0)])

    while queue:
        cur, distance = queue.popleft()
        distance += 1
        
        for n in graph[cur]:
            if visited[n]: continue

            visited[n] = True
            distance_from_source[n] = distance
            queue.append((n, distance))

    for s in sources:
        answer.append(distance_from_source[s])
                
    return answer