# https://school.programmers.co.kr/learn/courses/30/lessons/92335

from sys import setrecursionlimit
import math
setrecursionlimit(10 ** 6)

def solution(n, k):
    answer = 0
    n = convert(n, k)
    prev_zero_index = 0
    
    for i in range(len(n)):
        if n[i] == '0':
            if isPrime(int(n[prev_zero_index:i])): answer += 1
            prev_zero_index = i
    
    if n[-1] != '0':
        if isPrime(int(n[prev_zero_index:])): answer += 1

    return answer

def convert(n, k):
    if n < k: return str(n)
    return convert(n // k, k) + str(n % k)

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True