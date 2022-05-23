# https://www.acmicpc.net/problem/1562

MOD = 1000000000
MAX = (1<<10)-1
N = int(input())
cache = [[0] * (MAX+1) for _ in range(10)]

for i in range(1, 10):
    cache[i][1 << i] = 1

for _ in range(2, N+1):
    next_cache = [[0] * (MAX+1) for _ in range(10)]

    for i in range(10):
        for j in range(MAX+1):
            if i > 0:
                next_cache[i][j | (1 << i)] = (next_cache[i][j | (1 << i)] + cache[i-1][j]) % MOD
            if i < 9:
                next_cache[i][j | (1 << i)] = (next_cache[i][j | (1 << i)] + cache[i+1][j]) % MOD
 
    cache = next_cache

print(sum(cache[i][MAX] for i in range(10)) % MOD)