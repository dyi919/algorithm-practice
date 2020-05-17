import math

def Sieve(n):
    total = 0
    prime = [True for _ in range(n + 1)]
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    for x in prime:
        if x: total += 1
            
    return total

n = int(input())

while n != 0:
    print(Sieve(n * 2) - Sieve(n))
    n = int(input())