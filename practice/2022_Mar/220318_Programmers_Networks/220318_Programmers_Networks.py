import collections

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    while False in visited:
        start = visited.index(False)
        q = collections.deque([start])
        while q:
            v = q.popleft()
            visited[v] = True
            for i in range(n):
                if computers[v][i] == 1 and not visited[i]:
                    q.append(i)
        answer += 1
    return answer