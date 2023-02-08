# https://school.programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

def solution(board):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    N = len(board)
    visited = set()
    answer = 0
    
    def is_empty(p):
        nonlocal board
        return 0 <= p[0] < N and 0 <= p[1] < N and board[p[0]][p[1]] != 1
    
    def rotate(p1, p2):
        nonlocal board
        n_list = []
        x_diff = p2[1] - p1[1]

        for i in [-1, 1]:
            if x_diff != 0:
                if is_empty([p1[0] + i, p1[1]]) and is_empty([p2[0] + i, p2[1]]):
                    n_list.append([p1, [p1[0] + i, p1[1]]])
                    n_list.append([p2, [p2[0] + i, p2[1]]])
            else: 
                if is_empty([p1[0], p1[1] + i]) and is_empty([p2[0], p2[1] + i]):
                    n_list.append([[p1[0], p1[1] + i], p1])
                    n_list.append([[p2[0], p2[1] + i], p2])
                    
        return n_list
    
    queue = deque()
    queue.append([[0, 0], [0, 1], 0])
    visited.add((0, 0, 0, 1))
    
    while queue:
        p1, p2, time = queue.popleft()
        
        if p1 == [N - 1, N - 1] or p2 == [N - 1, N - 1]:
            return time
        
        for i in range(4):
            n1, n2 = [p1[0] + dx[i], p1[1] + dy[i]], [p2[0] + dx[i], p2[1] + dy[i]]
            
            if is_empty(n1) and is_empty(n2) and (n1[0], n1[1], n2[0], n2[1]) not in visited:
                visited.add((n1[0], n1[1], n2[0], n2[1]))
                queue.append([n1, n2, time + 1])
            
        n_list = rotate(p1, p2)
        for n in n_list:
            n1, n2 = n
            if (n2[0] < n1[0]) or (n2[0] == n1[0] and n2[1] < n1[1]):
                n1, n2 = n2, n1

            if is_empty(n1) and is_empty(n2) and (n1[0], n1[1], n2[0], n2[1]) not in visited:
                visited.add((n1[0], n1[1], n2[0], n2[1]))
                queue.append([n1, n2, time + 1])

    return answer