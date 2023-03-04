# https://school.programmers.co.kr/learn/courses/30/lessons/160585

def check_win(board, player):
    R, C = len(board), len(board[0])
    
    for row in board:
        start = row[0]
        if start != player: continue

        for col in row:
            if col != start:
                break
        else:
            return True
        
    for c in range(C):
        start = board[0][c]
        if start != player: continue

        for row in board:
            if row[c] != start:
                break
        else: 
            return True
    
    start = board[0][0]
    if start == player: 
        for i in range(R):
            if board[i][i] != start:
                break
        else:
            return True

    start = board[0][-1]
    if start == player: 
        for i in range(R):
            if board[i][R - 1 - i] != start:
                break
        else:
            return True
    
    return False
        
def solution(board):
    count_O, count_X = 0, 0
    
    for row in board:
        for col in row:
            if col == 'O':
                count_O += 1
            elif col == 'X':
                count_X += 1
    
    diff = count_O - count_X

    if diff < 0 or 1 < diff: return 0
    else: 
        if diff == 0 and check_win(board, 'O'): return 0
        if diff == 1 and check_win(board, 'X'): return 0
    
    return 1