# https://school.programmers.co.kr/learn/courses/30/lessons/148652

def get_count(n, x):
    total_count = 0
    
    while x > 5:
        divisor = 5 ** n
        multiplier = 4 ** n
        
        count, x = divmod(x, divisor)
        
        if count >= 3: 
            total_count += multiplier * (count - 1)
        else:
            total_count += multiplier * count
            
        if count == 2:
            return total_count
        
        n -= 1
        
    if x >= 3:
        x -= 1
    
    total_count += x

    return total_count

def solution(n, l, r):
    return get_count(n, r) - get_count(n, l - 1)
    
    