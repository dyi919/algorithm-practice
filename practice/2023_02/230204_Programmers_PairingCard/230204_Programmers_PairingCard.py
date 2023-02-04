# https://school.programmers.co.kr/learn/courses/30/lessons/72415

from collections import deque
    
def get_moves(board, start, end):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    if start == end: return 0

    queue, visited = deque([[start[0], start[1], 0]]), {start}

    while queue:
        x, y, moves = queue.popleft()

        for i in range(4):
            cx, cy = x, y
            nx, ny = x + dx[i], y + dy[i]
            
            while True:
                cx, cy = cx + dx[i], cy + dy[i]
                if not (0 <= cx < 4 and 0 <= cy < 4):
                    cx, cy = cx - dx[i], cy - dy[i]
                    break

                if not board[cx][cy] == 0: break

            if (nx, ny) == end or (cx, cy) == end:
                return moves + 1

            if (0 <= nx < 4 and 0 <= ny < 4) and (nx, ny) not in visited:
                queue.append((nx, ny, moves + 1))
                visited.add((nx, ny))

            if (cx, cy) not in visited:
                queue.append((cx, cy, moves + 1))
                visited.add((cx, cy))

def dfs(board, pos, moves, cards, pos_list):
    answer = 10 ** 9

    if not cards:
        return moves
    
    for i in range(len(cards)):
        c1, c2 = pos_list[cards[i]]
        
        c1_moves = moves + get_moves(board, pos, c2) + get_moves(board, c2, c1) + 2
        c2_moves = moves + get_moves(board, pos, c1) + get_moves(board, c1, c2) + 2

        board[c1[0]][c1[1]] = 0
        board[c2[0]][c2[1]] = 0
        
        if c1_moves < c2_moves:
            answer = min(dfs(board, c1, c1_moves, cards[:i] + cards[i + 1:], pos_list), answer)
        else:
            answer = min(dfs(board, c2, c2_moves, cards[:i] + cards[i + 1:], pos_list), answer)
        
        board[c1[0]][c1[1]] = cards[i]
        board[c2[0]][c2[1]] = cards[i]
    
    return answer
    
def solution(board, r, c):
    answer = 10 ** 9
    pos_list = [[] for _ in range(7)]
    remaining_cards = []
    
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                pos_list[board[i][j]].append((i, j))
    
    for i in range(1, 7):
        if pos_list[i]:
            remaining_cards.append(i)
    
    return dfs(board, (r, c), 0, remaining_cards, pos_list)