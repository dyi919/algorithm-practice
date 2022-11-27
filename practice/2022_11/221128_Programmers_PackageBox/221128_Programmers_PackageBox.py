# https://school.programmers.co.kr/learn/courses/30/lessons/131704

from collections import deque

def solution(order):
    answer = 0
    s = deque()
    pos = 0
    package_no = 1
    
    while package_no <= len(order):
        if package_no == order[pos]:
            answer += 1
            pos += 1
            package_no += 1
        elif s and s[-1] == order[pos]:
            s.pop()
            answer += 1
            pos += 1
        else:
            s.append(package_no)
            package_no += 1

    while s and s[-1] == order[pos]:
        s.pop()
        answer += 1
        pos += 1
    
    return answer