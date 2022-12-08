# https://school.programmers.co.kr/learn/courses/30/lessons/142085

from heapq import heappop, heappush, heapify

def solution(n, k, enemy):
    heap = []
    heapify(heap)
    
    answer = 0
    
    for e in enemy:
        heappush(heap, -e)

        if n < e:
            while heap and k > 0 and n < e:
                n -= heappop(heap)
                k -= 1
            if n < e:
                break
        
        n -= e
        answer += 1
    
    return answer