# https://school.programmers.co.kr/learn/courses/30/lessons/72414

def time_to_s(time):
    return get_h(time) * 60 * 60 + get_m(time) * 60 + get_s(time)

def get_h(time):
    return int(time[:2])

def get_m(time):
    return int(time[3:5])

def get_s(time):
    return int(time[6:8])

def split_time(time):
    return [time[:8], time[9:]]
    
def s_to_time(s):
    m = s // 60
    s %= 60
    h = m // 60
    m %= 60
    
    return str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
    
def solution(play_time, adv_time, logs):
    play_s = time_to_s(play_time)
    adv_s = time_to_s(adv_time)
    
    cache = [0] * (play_s + 1)
    
    for log in logs:
        log_start, log_end = split_time(log)
        cache[time_to_s(log_start)] += 1
        cache[time_to_s(log_end)] -= 1
    
    for i in range(1, play_s + 1):
        cache[i] += cache[i - 1]
        
    for i in range(1, play_s + 1):
        cache[i] += cache[i - 1]
        
    max_s = cache[adv_s]
    answer = 0
        
    for start_s in range(play_s - adv_s + 1):
        end_s = start_s + adv_s
        sum_s = cache[end_s] - cache[start_s]
        
        if sum_s > max_s:
            max_s = sum_s
            answer = start_s + 1
        
    return s_to_time(answer)