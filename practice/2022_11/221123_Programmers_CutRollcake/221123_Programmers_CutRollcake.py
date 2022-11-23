# https://school.programmers.co.kr/learn/courses/30/lessons/132265

def solution(topping):
    answer = 0
    count1 = 0
    count2 = 0
    dict1 = {}
    dict2 = {}
    
    for t in topping:
        if t not in dict2:
            dict2[t] = 1
            count2 += 1
        else:
            dict2[t] += 1
    
    for t in topping:
        dict2[t] -= 1
        if dict2[t] == 0:
            count2 -= 1
        if t not in dict1:
            dict1[t] = 1
            count1 += 1
        if count1 == count2: answer +=  1
        
    return answer