# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons, num_dungeons=0):
    if len(dungeons) == 0:
        return num_dungeons
    
    cur_max = num_dungeons
    
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and k >= dungeons[i][1]:
            cur_max = max(cur_max, solution(k-dungeons[i][1], dungeons[:i]+dungeons[i+1:], num_dungeons+1))

    return cur_max