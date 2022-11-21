# https://school.programmers.co.kr/learn/courses/30/lessons/118667#

from collections import deque

def solution(queue1, queue2):
    if sum(queue1 + queue2) % 2 == 1:
        return -1
    
    queue1, queue2 = deque(queue1), deque(queue2)
    MAX_COUNT = len(queue1) * 3 - 2
    sum1, sum2 = sum(queue1), sum(queue2)
    count = 0
    
    while count < MAX_COUNT:
        if sum1 == sum2:
            return count
        
        if sum1 < sum2: 
            queue1, queue2 = queue2, queue1
            sum1, sum2 = sum2, sum1
        
        element = queue1.popleft()
        queue2.append(element)
        sum1 -= element
        sum2 += element
        count += 1
    
    return -1