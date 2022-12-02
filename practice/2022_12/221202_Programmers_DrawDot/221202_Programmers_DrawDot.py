# https://school.programmers.co.kr/learn/courses/30/lessons/140107

def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        answer += ((d ** 2 - i ** 2) ** 0.5) // k + 1
        
    return answer