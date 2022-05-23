MOD = 1000000007

cache = [0] * (2501)
cache[0] = 1
cache[1] = 1

for i in range(2, 2501):
    for j in range(i):
        cache[i] += (cache[j] * cache[i-j-1]) % MOD
        cache[i] = cache[i] % MOD

T = int(input())
for _ in range(T):
    L = int(input())
    if L % 2 == 1:
        print("0")
        continue
    L //= 2
    
    print(cache[L])