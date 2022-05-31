# https://www.acmicpc.net/problem/11726

MOD = 10007

n = int(input())

if n <= 3:
    print(n)

else:
    cache = [0] * (n+1)
    cache[1] = 1
    cache[2] = 2

    for i in range(3, n+1):
        cache[i] = (cache[i-1] + cache[i-2]) % MOD

    print(cache[n])
