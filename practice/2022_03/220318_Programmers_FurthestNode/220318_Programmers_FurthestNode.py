# https://programmers.co.kr/learn/courses/30/lessons/49189

import collections, sys
def solution(n, edge):
    answer = 0
    d = collections.defaultdict()
    for s, e in edge:
        if s in d:
            d[s].append(e)
        else:
            d[s] = [e]
        if e in d:
            d[e].append(s)
        else:
            d[e] = [s]
    visited = [-1] * (n+1)
    q = collections.deque([(1, 0)])
    while q:
        node, dist = q.popleft()
        if visited[node] != -1:
            continue
        visited[node] = dist
        dist += 1
        for neighbor in d[node]:
            if visited[neighbor] == -1:
                q.append((neighbor, dist))
    visited.sort()
    answer = n-visited.index(max(visited))+1
    return answer