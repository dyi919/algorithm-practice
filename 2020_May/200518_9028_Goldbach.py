prime = [True for x in range(10000)]
i = 2
while i * i < 10000:
    if prime[i]:
        for j in range(i + i, 10000, i):
            prime[j] = False
    i += 1

t = int(input())

for _ in range(t):
    n = int(input())
    i = n // 2
    while i >= 2:
        if prime[i] and prime[n - i]:
            print(i, n - i)
            break
        i -= 1