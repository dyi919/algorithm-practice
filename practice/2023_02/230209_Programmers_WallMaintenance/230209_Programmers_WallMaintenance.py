# https://school.programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations

def solution(n, weak, d):
    num_friends = len(d)
    num_weak = len(weak)
    
    dist_comb = list(permutations(d, num_friends))
    
    next_weak_dist = [weak[i + 1] - weak[i] for i in range(num_weak - 1)]
    next_weak_dist.append(weak[0] + (n - weak[-1]))

    min_friends = 9
    
    for dist in dist_comb:
        for max_friends in range(1, min(num_friends + 1, min_friends)):       
            for start_idx in range(num_weak):
                weak_idx = start_idx
                end_idx = num_weak - 1 if start_idx == 0 else start_idx - 1
                friend_idx = 0
                remaining_dist = dist[0]

                while weak_idx != end_idx:
                    if remaining_dist < next_weak_dist[weak_idx]:
                        friend_idx += 1
                        weak_idx += 1
                        if weak_idx == num_weak: weak_idx = 0

                        if friend_idx == max_friends:
                            break

                        remaining_dist = dist[friend_idx]
                        continue
                    
                    remaining_dist -= next_weak_dist[weak_idx]               
                    
                    weak_idx += 1
                    if weak_idx == num_weak: weak_idx = 0
                    
                else: min_friends = min(min_friends, max_friends)

    return min_friends if min_friends < 9 else -1