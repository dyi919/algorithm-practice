# Gets prime numbers between two integers using the sieve of Eratosthenes

m, n = map(int, input().split())

d = [0] * (n + 1)
d[0] = 1
d[1] = 1

for i in range(2, n + 1):
    if d[i] == 0: p = 2 * i
    else: continue

    while p < n + 1:
        if d[p] == 0: d[p] = 1
        p += i

for i in range(m, n + 1):
    if d[i] == 0: print(i)