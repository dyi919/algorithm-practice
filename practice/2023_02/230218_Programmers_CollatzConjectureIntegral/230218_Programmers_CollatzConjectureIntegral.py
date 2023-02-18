# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def get_sequence(k):
    seq = [k]
    
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k *= 3
            k += 1
            
        seq.append(k)
        
    return seq

def get_cumulative_area(seq, L):
    cumulative_area = [0]
    
    for i in range(1, L):
        current_area = (seq[i - 1] + seq[i]) / 2
        cumulative_area.append(cumulative_area[i - 1] + current_area)

    return cumulative_area

def solution(k, ranges):
    answer = []
    seq = get_sequence(k)
    L = len(seq)
    cumulative_area = get_cumulative_area(seq, L)
    
    for a, b in ranges:
        start = a
        end = L - 1 + b
        
        if start > end:
            answer.append(-1)
            continue
        
        answer.append(cumulative_area[end] - cumulative_area[start])
    
    return answer