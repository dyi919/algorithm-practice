# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    s_list = list(map(int, s.split(' ')))
    return (' ').join([str(min(s_list)), str(max(s_list))])