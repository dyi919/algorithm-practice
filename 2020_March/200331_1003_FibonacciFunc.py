# calculate how many times fibonacci(0) and fibonacci(1) are executed

cache = [0] * 41
cache[0] = 1
cache[1] = 1

def fib(num):
    if cache[num] == 0:
        cache[num] = fib(num - 1) + fib(num - 2)
        return cache[num]
    else: return cache[num]

t = int(input())

for i in range(t):
    n = int(input())
    if n == 0: print(1, 0)
    elif n == 1: print(0, 1)
    else:
        fib(n)
        print(cache[n - 2], cache[n - 1])