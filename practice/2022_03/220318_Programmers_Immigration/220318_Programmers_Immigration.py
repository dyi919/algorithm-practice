# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    l, r = 1, max(times) * n
    while l <= r:
        people = 0
        mid = (l + r) // 2
        for time in times:
            people += mid // time
            if people >= n:
                break
        if people < n:
            l = mid+1
        else:
            answer = mid
            r = mid-1
    return answer