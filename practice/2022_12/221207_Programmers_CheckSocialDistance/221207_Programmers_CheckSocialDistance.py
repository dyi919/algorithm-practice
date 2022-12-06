# https://school.programmers.co.kr/learn/courses/30/lessons/81302

from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def check_place(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] != 'P':
                continue
            if bfs(i, j, place) == 0:
                return 0
    return 1
                
    
def bfs(x, y, place):
    queue = deque()
    queue.append([x, y, 0])
    visited = [[False] * 5 for _ in range(5)]
    visited[x][y] = True

    while queue:
        cx, cy, d = queue.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True
                if place[nx][ny] == 'P':
                    return 0
                elif place[nx][ny] == 'X':
                    continue
                elif d < 1:
                    queue.append([nx, ny, d+1])
    
    return 1

def solution(places):
    answer = []
    """
    for each place get participant position
    for each participant, bfs while depth < 3
    while bfs, if X then safe
    """
    
    for place in places:
        answer.append(check_place(place))
        
    return answer