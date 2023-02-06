from collections import Counter

def solution(a):
    N = len(a)
    
    if N == 1: 
        return 0
    
    c = Counter(a)
    answer = -1
    
    for k, v in c.items():
        if v * 2 <= answer:
            continue
        
        length = 0
        i = 0
        
        while i < N - 1:
            if (a[i] != k and a[i + 1] != k) or (a[i] == a[i + 1]):
                i += 1
                continue
            
            length += 2
            i += 2
        
        answer = max(length, answer)
        
    return answer