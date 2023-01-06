import sys
sys.setrecursionlimit(10 ** 6)

def add_leading_zeroes(bin_str):
    L = len(bin_str)
    total_digits = 1
    
    while total_digits < L:
        total_digits *= 2
        total_digits += 1
        
    return '0' * (total_digits - L) + bin_str

def is_valid(bin_str):
    L = len(bin_str)
    if L == 1: return True

    mid = L // 2
    
    if bin_str[mid] == '0':
        for c in bin_str:
            if c == '1': return False
        return True
        
    return is_valid(bin_str[:mid]) and is_valid(bin_str[mid + 1:])
    
def solution(numbers):
    answer = []
    
    for number in numbers:
        bin_str = bin(number)[2:]
        bin_str = add_leading_zeroes(bin_str)
        answer.append(1 if is_valid(bin_str) else 0)
            
    return answer