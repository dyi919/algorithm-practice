# https://school.programmers.co.kr/learn/courses/30/lessons/42628

from heapq import heapify, heappush

def solution(operations):
    pq = []
    heapify(pq)
    
    for op in operations:
        operation, value = op.split(" ")
        value = int(value)
        
        if operation == 'I':
            heappush(pq, value)
            pq.sort()
            continue
        
        if value == 1:
            pq = pq[:-1]
        elif len(pq) == 0:
            continue
        else:
            pq = pq[1:]
    
    return [0, 0] if len(pq) == 0 else [pq[-1], pq[0]]