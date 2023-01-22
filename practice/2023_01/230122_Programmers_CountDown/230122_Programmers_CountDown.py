# https://school.programmers.co.kr/learn/courses/30/lessons/131129

from collections import deque
INF = 10 ** 9

def initScores():
    scores = [50]
    
    for i in range(1, 21):
        scores.extend([i, i * 2, i * 3])
    
    scores = list(set(scores))
    
    return scores

def isSingleOrBull(score):
    return 1 <= score <= 20 or score == 50

def solution(target):
    scores = initScores()
    cache = [[INF, 0] for _ in range(target + 1)]
    cache[0] = [0, 0]
    queue = deque([0])
    min_num = INF

    while queue:
        current_score = queue.popleft()
        current_num = cache[current_score][0]
        if current_num > min_num: break
        next_num = current_num + 1

        for score in scores:
            next_score = current_score + score
            next_sum = 1 if isSingleOrBull(score) else 0
            next_sum += cache[current_score][1]
            
            if next_score == target: min_num = next_num
            if next_score > target: break
            if cache[next_score][0] < next_num or cache[next_score][1] > next_sum: continue
            
            if cache[next_score][0] > next_num:
                queue.append(next_score)
            cache[next_score] = [next_num, next_sum]

    return cache[target]