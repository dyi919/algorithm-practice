# https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    answer = 0
    
    sorted_targets = sorted(targets, key=lambda x: x[1])
    prev = -1
    
    for i in range(len(sorted_targets)):
        if sorted_targets[i][0] >= prev:
            answer += 1
            prev = sorted_targets[i][1]
            
    return answer