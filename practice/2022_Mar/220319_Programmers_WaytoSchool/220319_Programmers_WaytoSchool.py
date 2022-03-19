# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    def dp(i, j):
        if cache[i][j] == 0:
            cache[i][j] += dp(i-1, j) if i-1 > 0 and cache[i-1][j] != -1 else 0
            cache[i][j] += dp(i, j-1) if j-1 > 0 and cache[i][j-1] != -1 else 0
            cache[i][j] %= MOD
        return cache[i][j]
    
    MOD = 1000000007
    answer = 0
    cache = [[0] * (n+1) for _ in range(m+1)]
    cache[1][1] = 1
    for i, j in puddles:
        cache[i][j] = -1
        
    dp(m, n)
    
    return cache[m][n]