# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []
    
    start_row = left // n + 1
    start_col = left % n + 1
    end_row = right // n + 1
    end_col = right % n + 1
    
    for i in range(start_row, end_row+1):
        j_from = start_col if i == start_row else 1
        j_to = end_col+1 if i == end_row else n+1
        for j in range(j_from, j_to):
            answer.append(max(i, j))
        
    return answer