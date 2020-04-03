# G(n) = G(n - 1) + G(n - 2) + G(n - 3)

base = [0, 1, 1]

def fib(n, prev: list):
    if n == 0:
        return 0
    if n < 3:
        return 1
    
    if n == 3: 
        return sum(prev)
    
    return fib(n - 1, [prev[1], prev[2], sum(prev)])

for i in range(10):
    print(i,":", fib(i, base))
