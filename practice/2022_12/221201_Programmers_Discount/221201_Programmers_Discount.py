# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    want_dict = {}
    discount_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
            
    for i in range(10):
        if discount[i] in discount_dict:
            discount_dict[discount[i]] += 1
        else:
            discount_dict[discount[i]] = 1
    
    days = 0
    
    if want_dict == discount_dict:
        days += 1
    
    for i in range(len(discount)-10):
        discount_dict[discount[i]] -= 1
        if discount_dict[discount[i]] == 0:
            del discount_dict[discount[i]]
        if discount[i+10] in discount_dict:
            discount_dict[discount[i+10]] += 1
        else:
            discount_dict[discount[i+10]] = 1
        if want_dict == discount_dict:
            days += 1
    return days