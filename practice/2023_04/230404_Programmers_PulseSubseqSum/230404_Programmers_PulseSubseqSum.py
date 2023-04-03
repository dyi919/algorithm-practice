# https://school.programmers.co.kr/learn/courses/30/lessons/161988

def solution(sequence):
    L = len(sequence)
    max_sum = float('-inf')
    
    for initial_pulse in [1, -1]:
        cache = [float('-inf')] * L
        pulse_multiplier = [initial_pulse, -initial_pulse]
        pulse_sequence = [num * pulse_multiplier[i % 2] for i, num in enumerate(sequence)]
        cache[0] = pulse_sequence[0]
        
        for i in range(1, L):
            cache[i] = max(cache[i - 1] + pulse_sequence[i], pulse_sequence[i])
        
        max_sum = max(max(cache), max_sum)
    
    return max_sum