# https://school.programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

def solution(board):
    INF = 10 ** 9
    N = len(board)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    cache = [[[INF, INF] for _ in range(N)] for _ in range(N)]
    cache[0][0] = [0, 0]
    
    def within_boundary(x, y):
        return 0 <= nx < N and 0 <= ny < N
    
    def is_empty(x, y):
        return True if board[x][y] == 0 else False
    
    def get_cost(cx, cy, nx, ny, prev_direction):
        if prev_direction == 2: return 100
        if cx == nx and prev_direction == 0: return 100
        if cy == ny and prev_direction == 1: return 100
        return 600
    
    def get_direction(cx, cy, nx, ny):
        return 0 if cx == nx else 1
        
    
    queue = deque([])
    queue.append([0, 0, 2, 0])
    
    while queue:
        cx, cy, prev_direction, cost = queue.popleft()
        
        if cx == cy == N-1: continue
        
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if not within_boundary(nx, ny) or not is_empty(nx, ny): continue
            
            next_direction = get_direction(cx, cy, nx, ny)
            
            if cache[nx][ny][next_direction] > (next_cost := cost + get_cost(cx, cy, nx, ny, prev_direction)):
                cache[nx][ny][next_direction] = next_cost
                queue.append([nx, ny, next_direction, next_cost])
    
    return min(cache[N-1][N-1])