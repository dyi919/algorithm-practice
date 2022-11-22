# https://school.programmers.co.kr/learn/courses/30/lessons/135807

import math

def solution(arrayA, arrayB):
    def get_gcd(ls):
        ls.sort(reverse=True)
        gcd = ls[0]
        for i in ls[1:]:
            gcd = math.gcd(gcd, i)
        return gcd if gcd > 1 else 0
    
    def get_largest_divisor(gcd, target_list):
        if gcd == 0: return 0

        divisible = False
        for i in target_list:
            if i % gcd == 0:
                divisible = True
                break
            
        return gcd if not divisible else 0
    
    gcdA, gcdB = get_gcd(arrayA), get_gcd(arrayB)
    largest_divisor_A, largest_divisor_B = get_largest_divisor(gcdA, arrayB), get_largest_divisor(gcdB, arrayA)
    
    answer = max(largest_divisor_A, largest_divisor_B)
    
    return answer