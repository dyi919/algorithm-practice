# https://www.acmicpc.net/problem/2133

N = int(input())

if N % 2 == 1:
    print(0)

else:
    cache = [0] * (N+1)
    cache[0] = 1

    for i in range(2, N+1, 2):
        cache[i] += cache[i-2]
        for j in range(2, i+1, 2):
            cache[i] += cache[i-j] * 2

    print(cache[N])