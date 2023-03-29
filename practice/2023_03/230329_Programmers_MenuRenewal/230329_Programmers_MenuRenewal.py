# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):
    answer = []
    
    for course_num in course:
        order_count = {}
        
        for order in orders:
            combs = combinations(sorted(order), course_num)

            for comb in combs:
                comb_string = ('').join(comb)
                if comb_string in order_count:
                    order_count[comb_string] += 1
                else:
                    order_count[comb_string] = 1
        
        if len(order_count) == 0: continue
        
        max_count = max(order_count.values())
        answer.extend([k for k, v in order_count.items() if v == max(2, max_count)])
        
    return sorted(answer)