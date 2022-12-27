# https://school.programmers.co.kr/learn/courses/30/lessons/12979

import math

def solution(n, stations, w):
    answer = 0
    signal_range = w * 2 + 1
    len_stations = len(stations)

    for i in range(1, len_stations):
        interval = stations[i] - stations[i-1] - (w * 2) - 1
        
        if interval > 0:
            answer += math.ceil(interval / signal_range)
    
    for interval in [stations[0] - w - 1, n - stations[-1] - w]:
        if interval > 0:
            answer += math.ceil(interval / signal_range)

    return answer