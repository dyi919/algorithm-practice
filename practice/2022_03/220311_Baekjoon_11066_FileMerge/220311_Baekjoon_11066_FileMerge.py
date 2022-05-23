import sys

def dp(a, b):
    if a == b:
        return C[a]

    if cache[a][b] != -1:
        return cache[a][b]
    
    cache[a][b] = sys.maxsize
    rangeSum = preSum[b+1] - preSum[a]

    for i in range(a, b):
        cache[a][b] = min(dp(a, i) + dp(i+1, b) + rangeSum, cache[a][b])
    
    return cache[a][b]

T = int(input())

for _ in range(T):
    N = int(input())
    C = [int(x) for x in sys.stdin.readline().split()]
    cache = [[-1] * (N+1) for _ in range(N+1)]
    ans = sys.maxsize
    preSum = [0]
    
    total = 0
    for c in C:
        total += c
        preSum.append(total)

    for i in range(N-1):
        ans = min(dp(0, i) + dp(i+1, N-1), ans)
    print(ans)
    

    