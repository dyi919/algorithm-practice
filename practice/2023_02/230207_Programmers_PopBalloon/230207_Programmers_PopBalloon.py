# https://school.programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    INF = 10 ** 9 + 1
    N = len(a)
    left_min, right_min = [INF] * N, [INF] * N
    
    min_val = INF
    
    for i in range(1, N):
        min_val = min(min_val, a[i - 1])
        left_min[i] = min_val
        
    min_val = INF
    
    for i in range(N - 2, -1, -1):
        min_val = min(min_val, a[i + 1])
        right_min[i] = min_val
    
    answer = 0
    
    for i in range(N):
        if left_min[i] < a[i] and right_min[i] < a[i]:
            continue
            
        answer += 1
        
    return answer
