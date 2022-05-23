def solution(triangle):
    def dp(i, j):
        if i >= height or j >= len(triangle[i]): return 0
        if cache[i][j] == -1:
            cache[i][j] = triangle[i][j] + max(dp(i+1, j), dp(i+1, j+1))
        return cache[i][j]
    
    height = len(triangle)
    cache = [[-1] * height for _ in range(height)]
    
    return dp(0, 0)