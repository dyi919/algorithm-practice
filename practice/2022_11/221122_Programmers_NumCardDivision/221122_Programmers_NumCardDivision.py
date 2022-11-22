# https://school.programmers.co.kr/learn/courses/30/lessons/135807

import math

def solution(arrayA, arrayB):
    def factorize(n):
        factors = []
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                factors.append(i)
                factors.append(n//i)
        factors.append(n)
        return sorted(factors, reverse=True)

    def get_gcd(ls):
        ls.sort(reverse=True)
        gcd = ls[0]
        for i in ls[1:]:
            gcd = math.gcd(gcd, i)
        return gcd if gcd > 1 else 0
    
    def get_largest_divisor(gcd, target_list):
        if gcd == 0: return 0
    
        cd_list = factorize(gcd)

        for i in cd_list:
            divisible = False
            for j in target_list:
                if j % i == 0:
                    divisible = True
                    break
            if not divisible: return i
            
        return 0
                    
    
    gcdA, gcdB = get_gcd(arrayA), get_gcd(arrayB)
    largest_divisor_A, largest_divisor_B = get_largest_divisor(gcdA, arrayB), get_largest_divisor(gcdB, arrayA)
    
    answer = max(largest_divisor_A, largest_divisor_B)
    
    return answer