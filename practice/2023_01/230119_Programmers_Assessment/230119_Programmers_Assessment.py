# https://school.programmers.co.kr/learn/courses/30/lessons/152995

from bisect import bisect_right

def solution(scores):
    answer = 0
    score = scores[0]
    ans_score = sum(score)
    scores_sorted = sorted(scores, reverse=True, key=lambda x: [x[0], -x[1]])
    total_scores = [sum(scores_sorted[0])]

    count = len(scores_sorted)
    prev = 0
    i = 1
    
    while i < count:
        prev_b, prev_p = scores_sorted[prev]
        cur_b, cur_p = scores_sorted[i]
            
        if prev_b > cur_b and prev_p > cur_p:
            if score == scores_sorted[i]: return -1
        else:
            total_scores.append(sum(scores_sorted[i]))
            prev = i
            
        i += 1
    
    total_scores.sort()
    return len(total_scores) - bisect_right(total_scores, ans_score) + 1