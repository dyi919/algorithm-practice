# https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque

def solution(maps):
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    R, C = len(maps), len(maps[0])
    S, E, L = [], [], []
    
    for i in range(R):
        for j in range(C):
            if maps[i][j] == 'S': S = (i, j)
            if maps[i][j] == 'E': E = (i, j)
            if maps[i][j] == 'L': L = (i, j)
    
    def bfs(start, target):
        visited = [[False] * C for _ in range(R)]
        queue = deque()
        queue.append([start, 0])
        visited[start[0]][start[1]] = True

        while queue:
            pos, time = queue.popleft()
            r, c = pos
            
            if r == target[0] and c == target[1]:
                return time

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and maps[nr][nc] != 'X':
                    visited[nr][nc] = True
                    queue.append([(nr, nc), time + 1])
            
        return -1
        
    StoL = bfs(S, L)
    LtoE = bfs(L, E)
    
    return StoL + LtoE if StoL != -1 and LtoE != -1 else -1