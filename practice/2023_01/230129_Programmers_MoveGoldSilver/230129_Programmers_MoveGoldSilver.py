# https://school.programmers.co.kr/learn/courses/30/lessons/86053

def solution(a, b, g, s, w, t):
    N = len(t)
    
    def check(mid):
        nonlocal a, b, g, s, w, t, N
        g_weight = 0
        s_weight = 0
        total_weight = 0
        
        for i in range(N):
            count = mid // (t[i] * 2)
            if mid % (t[i] * 2) >= t[i]:
                count += 1
            
            max_weight = min(count * w[i], g[i] + s[i])
            g_weight += min(max_weight, g[i])
            s_weight += min(max_weight, s[i])
            total_weight += max_weight
        
        return True if total_weight >= a + b and g_weight >= a and s_weight >= b else False

    start, end = 0, 10e9 * 2 * 10e5 * 2
    
    while start < end:
        mid = (start + end) // 2
        if check(mid):
            end = mid
        else:
            start = mid + 1
    
    return end