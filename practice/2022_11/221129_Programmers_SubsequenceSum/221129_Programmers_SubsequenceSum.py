# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    num_elements = len(elements)
    sum_list = []
    for i in range(num_elements):
        total = 0
        for j in range(num_elements):
            total += elements[(i+j)%num_elements]
            sum_list.append(total)
    sum_list = list(set(sum_list))
            
    return len(sum_list)