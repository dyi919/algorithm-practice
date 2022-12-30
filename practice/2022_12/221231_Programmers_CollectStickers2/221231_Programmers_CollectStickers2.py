import sys
sys.setrecurstionlimit(10 ** 6)

def dp(cache, n, sticker):
    if n >= len(cache):
        return 0
    
    if cache[n] > 0:
        return cache[n]

    cache[n] = max(sticker[n] + dp(cache, n+2, sticker), dp(cache, n+1, sticker))
    
    return cache[n]

def solution(sticker):
    N = len(sticker)
    
    if (N == 1): return sticker[0]
    
    cache_with_first = [0] * (N-1)
    cache_with_last = [0] * (N-1)
    
    dp(cache_with_first, 0, sticker[:-1])
    dp(cache_with_last, 0, sticker[1:])

    return max(cache_with_first[0], cache_with_last[0])