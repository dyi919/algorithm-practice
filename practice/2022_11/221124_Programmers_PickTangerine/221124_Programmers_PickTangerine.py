# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter

def solution(k, tangerine):
    answer = 0
    num_tangerine = 0
    i = 0
    counter = Counter(tangerine).most_common()
    for _, c in counter:
        num_tangerine += c
        answer += 1
        if num_tangerine >= k:
            break
        
    return answer