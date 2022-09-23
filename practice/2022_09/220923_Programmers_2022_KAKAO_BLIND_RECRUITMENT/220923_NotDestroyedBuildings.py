# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    sum_board = [[0] * (M+1) for _ in range(N+1)]
    
    for skill_type, r1, c1, r2, c2, degree in skill:
        sum_board[r1][c1] -= degree if skill_type == 1 else -degree
        sum_board[r1][c2+1] += degree if skill_type == 1 else -degree
        sum_board[r2+1][c1] += degree if skill_type == 1 else -degree
        sum_board[r2+1][c2+1] -= degree if skill_type == 1 else -degree
    
    for i in range(N):
        for j in range(M):
            sum_board[i][j+1] += sum_board[i][j]
            
    for i in range(N):
        for j in range(M):
            sum_board[i+1][j] += sum_board[i][j]
    
    for i in range(N):
        for j in range(M):
            board[i][j] += sum_board[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer