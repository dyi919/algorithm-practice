from sys import stdin, maxsize

def dp(n):
    if n in cache:
        return cache[n]
    if n < A:
        return maxsize
    if n == A:
        return cache[n]
    
    if n % 2 == 0 and (n-1) % 10 == 0:
        cache[n] = 1 + min(dp(n//2), dp((n-1)//10))
        return cache[n]
    elif n % 2 == 0:
        cache[n] = 1 + dp(n//2)
        return cache[n]
    elif (n-1) % 10 == 0:
        cache[n] = 1 + dp((n-1)//10)
        return cache[n]
    else:
        return maxsize

A, B = [int(i) for i in stdin.readline().split()]

cache = {A:1}
ans = dp(B)
print(ans if ans < maxsize else -1)